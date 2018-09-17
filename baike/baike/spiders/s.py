from scrapy.http import Request, FormRequest
from ..items import BaikeItem
from lxml import etree
import scrapy

i = 0

class BaikeSpider(scrapy.Spider):
    name = 'baike'

    inp = input("请输入关键字：")
 #   inp = '深圳'
    start_urls = ['https://baike.baidu.com/item/%s' % inp]

    def parse(self, response):

        global i
        i += 1

        tree = etree.HTML(response.text)
        print(response.url)

        item = BaikeItem()
        item['url'] = response.url;
        item['title'] = tree.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')[0]
        urls = tree.xpath('(//*[@class="para"])/a/@href')
        tmp = tree.xpath('//div[@class="main-content"]')[0]
        item['content'] = etree.tostring(tmp, encoding='utf-8', method='html').decode('utf-8')

        print('\n%s ==> %s'% (i,item['title']))
        yield item

        for url in urls:
        #    print(url)
            url = response.urljoin(url)
            if i>10000:
                self.crawler.engine.close_spider(self, 'closespider')
            else:
                yield scrapy.Request(url, callback=self.parse)



