#导入scrapy
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy

from ..items import QiubaiItem
from scrapy.http import Request

#创建糗百爬虫类
class QiuBaiSpider(scrapy.Spider):
    #定义爬虫的名字
	name = 'qiushi'
    #定义爬虫开始的URL
	
	
	start_urls=['http://www.qiushibaike.com/text/page/1']
	
	
	#处理爬取的信息
	def parse(self, response):
		
		for sel in response.xpath('//div[contains(@class,"article") and contains(@class, "untagged")]'):
			item = QiubaiItem()
			item['author'] = sel.xpath('normalize-space(div[@class="author clearfix"]/a[2]/h2/text())').extract()[0]
			item['author_logo'] = sel.xpath('div[@class="author clearfix"]/a[1]/img/@src').extract()[0]
			item['content'] = sel.xpath('normalize-space(a[@class="contentHerf"]/div/span/text())').extract()[0]
			item['vote'] = sel.xpath('div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()[0]
			item['comments'] = sel.xpath('div[@class="stats"]/span[@class="stats-comments"]/a/i/text()').extract()[0]
			item['article_id'] = sel.xpath('a[@class="contentHerf"]/@href').extract()[0].split('/article/',1)[1]
			
		#	print(''.join(item['author']), " ：\n",''.join(item['content']))
			
		
			yield(item)
		next_page = response.xpath("//ul[@class='pagination']/li/a/@href").extract()[-1]
		print("page => %s" % next_page)
		
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)