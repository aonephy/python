from scrapy.http import Request, FormRequest
from ..items import BaiduItem
from lxml import etree
import scrapy

i = 0

class BaiduSpider(scrapy.Spider):
    name = 'baidu'

    inp = input("请输入关键字：")
#    inp = '皮皮侠'
    start_urls = ['https://zhidao.baidu.com/search?word=%s' % inp]

    def parse(self, response):

        global i
        i += 1

        tree = etree.HTML(response.text)
        for sel in tree.xpath('//dt[@class="dt mb-4 line"]'):
            #print(response.url)
            url = sel.xpath('a/@href')[0]
            yield scrapy.Request(url, callback=self.spiderContent)


        if i > 5:
            self.crawler.engine.close_spider(self, 'closespider')

        else:
            print("【%s】" % i)
            next_page = sel.xpath('//a[@class="pager-next"]/@href')[0]
            if next_page is not None:
                next_page = response.urljoin(next_page)
                print(next_page)

                yield scrapy.Request(next_page, callback=self.parse)

    def spiderContent(self, response):

        print(response.url)
        item = BaiduItem()
        tree = etree.HTML(response.text)
        item['url'] = response.url
        item['question'] = tree.xpath('//*[contains(@class,"ask-title")]/text()')[0]
        tmp = tree.xpath('//div[contains(@class,"best-text")]')[0]
    #    tmp = tree.xpath('//div[contains(@class,"best-text")]/*[not(contains(@class,"wgt-best-mask"))]')[0]
        item['answer'] = etree.tostring(tmp,encoding='utf-8',method='html').decode('utf-8').replace('map="iknow/page.html?','src="//zhidao.baidu.com/html/map/page.html?')

      #  print(item)



        yield item

