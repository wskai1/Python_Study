# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os
import urllib.request

# 保存到JSON中
# class MyPipeline(object):
#     def open_spider(self, spider):
#         self.file = codecs.open('test.json', 'wb', encoding='utf-8')  ######### 重要2
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"  ####### 重要3
#         self.file.write(line)
#         return item
# 保存图片到指定文件夹
#
# class PicPipeline(object):
#     def process_item(self, item, spider):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#         req = urllib.request.Request(url=item['addr'],headers=headers)
#         res = urllib.request.urlopen(req)
#         file_name = os.path.join(r'E:\wsk\Python\Scrapy\my\my',item['name']+'.jpg')
#         with open(file_name,'wb') as fp:
#             fp.write(res.read())

# 保存到TXT
class TxtPipeline(object):
    def process_item(self, item, spider):
        file_name = "E:\wsk\Python\Scrapy\my\my.txt"  # 以追加的方式打开文件，不存在则创建
        # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，
        # 将其编码改为utf-8
        with open(file_name,'a',encoding='utf8') as f:
            name=item['name']
            url=item['url']
            f.write(str(name))
            f.write(str(url))
            f.write('\n')
        return item