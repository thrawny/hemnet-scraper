# -*- coding: utf-8 -*-

from urlparse import urlparse
import re
import scrapy
from hemnet.items import HemnetItem


BASE_URL = 'http://www.hemnet.se/salda/bostader?location_ids%5B%5D=17920'


def start_urls(stop):
    return ['{}&page={}'.format(BASE_URL, x) for x in xrange(1, stop)]


class HemnetSpider(scrapy.Spider):
    name = 'hemnetspider'
    rotate_user_agent = True

    start_urls = start_urls(10)

    def parse(self, response):
        urls = response.css('#search-results li > div > a::attr("href")')
        for url in urls:
            yield scrapy.Request(url.extract(), self.parse_detail_page)

    def parse_detail_page(self, response):
        item = HemnetItem()

        broker = response.css('.broker-info > p')[0]
        property_attributes = get_property_attributes(response)

        item['url'] = response.url
        item['type'] = urlparse(response.url).path.split('/')[2].split('-')[0]

        item['rooms'] = property_attributes.get(u'Antal rum', '').replace(u' rum', u'')

        try:
            fee = int(property_attributes.get(u'Avgift/månad', '').replace(u' kr/m\xe5n', '').replace(u'\xa0', u''))
        except ValueError:
            fee = ''
        item['monthly_fee'] = fee

        item['square_meters'] = float(property_attributes.get(u'Boarea', '').split(' ')[0].replace(',', '.'))
        try:
            cost = int(property_attributes.get(u'Avgift/månad', '').replace(u' kr/m\xe5n', '').replace(u'\xa0', u''))
        except ValueError:
            cost = ''
        item['cost_per_year'] = cost
        item['year'] = property_attributes.get(u'Byggår', '')  # can be '2008-2009'

        item['broker_name'] = broker.css('strong::text').extract_first()
        item['broker_phone'] = strip_phone(broker.css('.phone-number::attr("href")').extract_first())

        item['broker_firm'] = response.css('.broker-info > p')[1].css('strong::text').extract_first()

        raw_price = response.css('.sold-property-price > span::text').extract_first()
        item['price'] = price_to_int(raw_price)

        selling = response.css('.selling-statistics > li > strong::text').extract()
        try:
            item['price_per_square_meter'] = int(selling[0].replace(u'\xa0', '').split(' ')[0])
            item['asked_price'] = price_to_int(selling[1])
            item['price_trend_flat'], item['price_trend_percentage'] = price_trend(selling[2])
        except IndexError:
            pass

        detail = response.css('.sold-property-details')[0]

        item['sold_date'] = detail.css('.metadata > time::attr("datetime")').extract_first()
        item['address'] = detail.css('h1::text').extract_first()
        item['geographic_area'] = detail.css('.area::text').extract_first().strip()

        yield item


def get_property_attributes(response):
    a = response.css('ul.property-attributes > li::text').extract()
    x = [x.strip() for x in a]
    b = response.css('ul.property-attributes > li > strong::text').extract()

    return dict(zip(x, b))


def price_to_int(price_text):
    return int(price_text.replace(u'\xa0', u'').replace(u' kr', u'').encode())


def strip_phone(phone_text):
    if phone_text:
        return phone_text.replace(u'tel:', u'')
    else:
        return u''


def price_trend(price_text):
    r = '(?P<sign>[+-])(?P<flat>\d*)\([+-](?P<percentage>\d*)\%\)$'

    temp = price_text.replace(u'\xa0', '').replace(' ', '').replace('kr', '')

    matches = re.search(r, temp)

    sign = matches.group('sign')
    flat = int('{}{}'.format(sign, matches.group('flat')))
    percentage = int('{}{}'.format(sign, matches.group('percentage')))
    return flat, percentage


def rooms(rooms_text):
    pass
