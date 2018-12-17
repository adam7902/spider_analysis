# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    # info = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    typ = scrapy.Field()
    image_link = scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    words = scrapy.Field()



