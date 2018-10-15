from scrapy.http import Request, FormRequest
from lxml import etree
import scrapy

i = 0

class aonephySpider(scrapy.Spider):
    name = 'aonephy'
    start_urls = ['http://aonephy.top/bbs/login.php']

    def parse(self, response):
        print('【%s】 start...' % i)

        yield scrapy.FormRequest.from_response(
            response,  # 传入response对象,自动解析
            # 可以通过xpath来定位form表单,当前页只有一个form表单时,将会自动定位
            formxpath='//div[@id="login_box"]/form',
            formdata={'user': '6', 'password': '698d51a19d8a121ce581499d7b701668'},
            callback=self.visit
        )
    def visit(self,response):
        url = "http://aonephy.top/blog/list.php?id=1"
        yield scrapy.Request(url, callback=self.getContent)

    def getContent(self, response):
        print(response.url)
        global i
        i += 1
        tree = etree.HTML(response.text)

        urls = tree.xpath('//div[@class="media-body"]//a/@href')

        for url in urls:

            url = response.urljoin(url)

            if i>5:
                self.crawler.engine.close_spider(self, 'closespider')
            else:
                yield scrapy.Request(url, callback=self.getContent)
