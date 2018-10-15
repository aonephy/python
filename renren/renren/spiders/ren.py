from scrapy.http import Request, FormRequest
from ..items import RenrenItem
from scrapy.http import Request
from lxml import etree
import scrapy
import re
 
class Login3Spider(scrapy.Spider):
	name = 'ren'
	start_urls = ['http://www.renren.com/PLogin.do']
 
	
	def parse(self, response):
		yield scrapy.FormRequest.from_response(
			response, # 传入response对象,自动解析
			# 可以通过xpath来定位form表单,当前页只有一个form表单时,将会自动定位
			formxpath='//form[@id="login_box"]',
			formdata={'email': 'anjinfeng123@163.com', 'password': '043252410'},
			callback=self.parse_login
		)
 
	def parse_login(self,response):
		url = "http://www.renren.com/125723999/profile"
		yield scrapy.Request(url, callback=self.getContent)
	
		
	def getContent(self,response):
		tree = etree.HTML(response.text)
		i = 0
	
		for sel in tree.xpath('//div[@class="visit-special-con"]//ul/li'):
			url = sel.xpath('//div[@class="share-friend"]/ul/li/a/@href')[i]
			item = RenrenItem()
			item['visit'] = sel.xpath('//div[@class="clearfix"]/ul/li/a/@href')
			item['share_friend'] = sel.xpath('//div[@class="share-friend"]/ul/li/a/@href')
			item['has_friend'] = sel.xpath('//div[@class="has-friend"]/ul/li/a/@href')			
			
		#	i = 1 + i
		#	print(url)
			request = scrapy.Request(url, callback=self.getInfo)			
			yield request
			
	def	getInfo(self,response):
	#	print(response.url)
		tree = etree.HTML(response.text)
		for sel in tree.xpath('//div[@class="tl-information"]/ul'):
			item = RenrenItem()
			item['name'] = sel.xpath('normalize-space(//*[@class="avatar_title no_auth"]/text())')
			item['img'] = sel.xpath('//*[@id="userpic"]/@src')
			item['url'] = response.url
			item['school'] = sel.xpath('li[@class="school"]/span/text()')
			if item['school']:
				item['school'] = item['school'][0].replace('就读于','')
			item['gender'] = sel.xpath('li[@class="birthday"]/span/text()')[0]
			item['birthday'] = sel.xpath('li[@class="birthday"]/span/text()')[1]
			if item['birthday']:
				item['birthday'] = item['birthday'].replace('，','')
			item['hometown'] = sel.xpath('li[@class="hometown"]/text()')
			if	item['hometown']:
				item['hometown'] = item['hometown'][0].replace('来自 ','')
			item['address'] = sel.xpath('li[@class="address"]/text()')
			if item['address']:
				item['address'] = item['address'][0].replace('现居 ','')
			print(item)
			yield(item)
	