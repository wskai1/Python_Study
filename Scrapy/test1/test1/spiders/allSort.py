import re

import scrapy
from scrapy import Selector, Request

from test1.items import CategoriesItem

key_word = ['book', 'e', 'channel', 'mvd', 'list']
Base_url = 'https://list.jd.com'
price_url = 'https://p.3.cn/prices/mgets?skuIds=J_'
comment_url = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=5&page=%s&pageSize=10'
favourable_url = 'https://cd.jd.com/promotion/v2?skuId=%s&area=1_72_2799_0&shopId=%s&venderId=%s&cat=%s'
class JD(scrapy.Spider):
    name="allSort"
    allowed_domains = ["jd.com"]
    start_urls = [
        "https://www.jd.com/allSort.aspx"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_category)

    def parse_category(self, response):
        """获取分类页"""
        selector = Selector(response)
        try:
            texts = selector.xpath(
                '//div[@class="category-item m"]/div[@class="mc"]/div[@class="items"]/dl/dd/a').extract()
            for text in texts:
                items = re.findall(r'<a href="(.*?)" target="_blank">(.*?)</a>', text)
                for item in items:
                    if item[0].split('.')[0][2:] in key_word:
                        if item[0].split('.')[0][2:] != 'list':
                            yield Request(url='https:' + item[0], callback=self.parse_category)
                        else:
                            categoriesItem = CategoriesItem()
                            categoriesItem['name'] = item[1]
                            categoriesItem['url'] = 'https:' + item[0]
                            categoriesItem['_id'] = item[0].split('=')[1].split('&')[0]
                            yield categoriesItem
                            # yield Request(url='https:' + item[0], callback=self.parse_list)
        except Exception as e:
            print('error:', e)