from scrapy.http import Request, FormRequest
import scrapy
import re
 
class Login3Spider(scrapy.Spider):
	name = 'ren-'
	start_urls = ['http://aonephy.top/music']
 
	
	def parse(self, response):
		yield scrapy.FormRequest.from_response(
			response, # 传入response对象,自动解析
			# 可以通过xpath来定位form表单,当前页只有一个form表单时,将会自动定位
			formxpath='//*[@id="login_box"]/form', 
			formdata={'user': '6', 'password': '698d51a19d8a121ce581499d7b701668'},
			callback=self.parse_login
		)
 
	def parse_login(self,response):
		url = "http://localhost/creditCard"
		yield scrapy.Request(url, callback=self.getContent)
	
		
	def getContent(self,response):
		for sel in response.xpath('//*'):
			tmp = sel.xpath('normalize-space(text())').extract()
			print(tmp)
