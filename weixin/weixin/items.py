# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeixinItem(scrapy.Item):
    # define the fields for your item here like:
    wxId = scrapy.Field()
    url = scrapy.Field()
    articleUrl = scrapy.Field()
    nickname = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pass
	
class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    pass