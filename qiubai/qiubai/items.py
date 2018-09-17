import scrapy

class QiubaiItem(scrapy.Item):
	# define the fields for your item here like:

	author      = scrapy.Field()    # 作者
	author_logo = scrapy.Field()    # 作者头像

	article_id  = scrapy.Field()    # 内容ID
	content     = scrapy.Field()    # 内容
	thumb       = scrapy.Field()    # 内容图片

	vote        = scrapy.Field()    # 赞人数
	comments    = scrapy.Field()    # 评论数
