# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class LianjiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    house_title = Field()
    house_community = Field()
    house_room = Field()
    house_area = Field()
    house_location = Field()
    house_price = Field()
    price_setp = Field()
