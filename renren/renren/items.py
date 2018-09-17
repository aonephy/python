# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrenItem(scrapy.Item):
    visit = scrapy.Field()    #
    share_friend = scrapy.Field()    #
    has_friend = scrapy.Field()    #
    img = scrapy.Field()    #
    name = scrapy.Field()    #
    url = scrapy.Field()    #
    school = scrapy.Field()    #
    work = scrapy.Field()    #
    gender = scrapy.Field()    #
    birthday = scrapy.Field()    #
    hometown = scrapy.Field()    #
    address = scrapy.Field()    #
	
