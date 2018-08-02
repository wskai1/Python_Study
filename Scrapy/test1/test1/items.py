# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class CategoriesItem(scrapy.Item):
    name = Field()  # 分类名称
    url = Field()  # 分类url
    _id = Field()  # 分类id
    index = Field()  # 分类的index