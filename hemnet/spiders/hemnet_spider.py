import scrapy

from hemnet.items import HemnetItem


class HemnetSpider(scrapy.Spider):
    name = 'hemnetspider'
    rotate_user_agent = True

    start_urls = ['http://www.hemnet.se/salda/bostader?location_ids%5B%5D=17920']

    def parse(self, response):
        urls = response.css('#search-results li > div > a::attr("href")')
        for url in urls[:2]:
            yield scrapy.Request(url.extract(), self.parse_detail_page)

    def parse_detail_page(self, response):
        item = HemnetItem()

        item['broker_name'] = response.css('.broker-info > p')[0].css('strong::text').extract_first()
        item['broker_firm'] = response.css('.broker-info > p')[1].css('strong::text').extract_first()

        raw_price = response.css('.sold-property-price > span::text').extract_first()
        item['price'] = price_to_int(raw_price)

        detail = response.css('.sold-property-details')[0]

        item['sold_date'] = detail.css('.metadata > time::attr("datetime")').extract_first()

        item['address'] = detail.css('h1::text').extract_first()
        item['geographic_area'] = detail.css('.area::text').extract_first().strip()

        item['rooms'] = int(detail.css('.property-attributes > li > strong::text').extract_first()[0])

        yield item


def price_to_int(price_text):
    return int(price_text.replace(u'\xa0', u'').replace(u' kr', u'').encode())
