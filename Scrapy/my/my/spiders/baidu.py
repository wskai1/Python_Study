import scrapy

from my.items import BaiduItem


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ['https://www.baidu.com/',]

    def parse(self, response):
        print("sssssssssss")
        lista = response.xpath('//*[@id="u1"]/a')
        for a in lista:
            item=BaiduItem()
            item['name']=a.xpath('text()').extract()
            item['url']=a.xpath('@href').extract()
            yield item