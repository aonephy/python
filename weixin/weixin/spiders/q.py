from scrapy.http import Request, FormRequest
from ..items import WeixinItem
from lxml import etree
import scrapy

class SogouSpider(scrapy.Spider):
	name = 'weixin'
#	inp = input("请输入微信公共号名称：")
	inp = '皮皮侠'
	start_urls = ['http://weixin.sogou.com/weixin?query=%s' % inp]
#	start_urls = ['http://localhost/sogou.html']
#	start_urls = ['https://zhidao.baidu.com/search?word=ppx']
 	
	def parse(self, response):
		
		tree = etree.HTML(response.text)
		
		print('start spider')
		
		for sel in tree.xpath('//div[@class="news-box"]/ul/li'):
		
			tmp = sel.xpath('dl[2]/dd/a/@href')
			if len(tmp):
			
				url = tmp[0]
			#	url = 'http://localhost/wx.html'
				yield scrapy.Request(url, callback=self.getArticle)
		
	#	next_page = tree.xpath('//a[@class="np"]/@href')[0]
	#	print(next_page)
		
	#	if next_page is not None:
	#		next_page = response.urljoin(next_page)
		#	print(next_page)
	#		yield scrapy.Request(next_page, callback=self.parse)
			
				
	def getArticle(self,response):
	#	print(response.url)
		tree = etree.HTML(response.text)
		
		for sel in tree.xpath('//div[@id="img-content"]'):
			item = WeixinItem()
			item['url'] = response.url
			item['title'] = sel.xpath('normalize-space(//h2[@id="activity-name"]/text())')
			item['nickname'] = sel.xpath('//strong[@class="profile_nickname"]/text()')[0]
			item['wxId'] = sel.xpath('//span[@class="profile_meta_value"]/text()')[0]
			if len(item['wxId'])>30:
				item['wxId'] = ''
			tmp = sel.xpath('//*[@id="js_content"]')[0]
			tmp = etree.tostring(tmp,encoding = "utf-8", method='html').decode('utf-8')
		#	tmp = etree.HTML(tmp)
			item['content'] = tmp
			
	#	print(item)	
		yield(item)
		
		