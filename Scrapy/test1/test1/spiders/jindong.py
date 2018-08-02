import scrapy


class JD(scrapy.Spider):
    name="Jd"
    allowed_domains = ["jd.com"]
    start_urls = [
        "https://www.jd.com/"
    ]

    def parse(self, response):
        print("sssssssssss")
        req = []
        list = response.xpath('//*[@id="J_cate"]/ul')
        for li in list.xpath('./li'):
            yield {
                'text':li.xpath('./a/text()').extract(),
                'href':li.xpath('./a/@href').extract()
            }
