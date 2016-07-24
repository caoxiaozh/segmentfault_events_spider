# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose,MapCompose ,TakeFirst


class SegmentfaultEventsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    icon = scrapy.Field()
    status = scrapy.Field()
    detail = scrapy.Field()
    join_link = scrapy.Field()
    link = scrapy.Field()
