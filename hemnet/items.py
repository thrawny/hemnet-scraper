# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HemnetItem(scrapy.Item):
    url = scrapy.Field()

    hemnet_id = scrapy.Field()

    broker_name = scrapy.Field()
    broker_phone = scrapy.Field()
    broker_email = scrapy.Field()

    broker_firm = scrapy.Field()
    broker_firm_phone = scrapy.Field()

    sold_date = scrapy.Field()

    price_per_square_meter = scrapy.Field()
    price = scrapy.Field()
    asked_price = scrapy.Field()
    price_trend_flat = scrapy.Field()
    price_trend_percentage = scrapy.Field()

    rooms = scrapy.Field()
    monthly_fee = scrapy.Field()
    square_meters = scrapy.Field()
    cost_per_year = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()

    address = scrapy.Field()
    geographic_area = scrapy.Field()
