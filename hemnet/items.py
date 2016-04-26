# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HemnetItem(scrapy.Item):
    broker_name = scrapy.Field()
    broker_firm = scrapy.Field()
    sold_date = scrapy.Field()
    price_per_square_meter = scrapy.Field()
    price = scrapy.Field()
    asked_price = scrapy.Field()
    rooms = scrapy.Field()
    monthly_fee = scrapy.Field()
    square_meter = scrapy.Field()
    cost_per_year = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    geographic_area = scrapy.Field()
