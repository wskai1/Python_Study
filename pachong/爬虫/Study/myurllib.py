# -*- coding:utf-8 -*-

# from bs4 import BeautifulSoup
import _thread
import re
import time

import urllib.request

# 建立一个爬虫的类



class spider:

    def __init__(self):
        # 首先确定加载的页数
        self.page = 1
        self.pages = []
        # 后面有循环
        self.loop = False

    # 扣除段子部分的代码
    # 这个部分大部分爬虫都是一样
    def getPage(self, page):
        # 糗事百科地址，这个不要弄错
        # 爬其他东西把地址换一下就可以
        # 这个部分是伪装成浏览器进入糗百的主页
        url = "http://m.qiushibaike.com/hot/page/" + page + '/'
        user_agent = 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url, headers=headers)
        myResponse = urllib.request.urlopen(req)
        # 抓取页面
        myPage = myResponse.read()
        # 对爬下来的内容进行解码，转换成Unicode编码
        unicodePage = myPage.decode('utf-8')
        # soup = BeautifulSoup(myResponse.read())
        # contents= soup.find_all('div class="content"','/div')
        # 还在学BS4爬东西，暂时没用到
        # 根据网页源代码的特点找出段子的内容
        # 标记为<class="content"></div>
        contents = re.findall('<div.*?class="content".*?>(.*?)</div>', unicodePage, re.S)
        list = []
        # 将段子保存进列表
        for content in contents:
            list.append(content.replace("\n", ""))
        return list

    # 如果页面中的段子已经扣完，想扣新的段子
    def loadPage(self):
        while self.loop:
            if len(self.pages) < 2:
                # 当加载的段子条数小于两条的时候，读取第二页第三页内容
                try:
                    # self.getPage返回的是list[]，已经是这一页所有的段子
                    myPage = self.getPage(str(self.page))
                    # 这是第二页的第一条
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print(u"无法链接糗事百科")
            else:
                time.sleep(1)

    def showPage(self, nowPage, page):
        # nowPage中只有一个元素，list遍历出来只打印出于nowPage中相同的元素
        for list in nowPage:
            print(u'第%d页\n' % page, list, '\n')
            next = input('>next\n')
            if next == "exit":
                self.loop = False
                print(u"已退出爬虫程序")
                break

    def start(self):
        self.loop = True
        page = self.page

        print(u"程序正在加载中,正在寻找段子,请稍后....\n")

        # 多线程是个坑，可以做很多事情
        _thread.start_new_thread(self.loadPage, ())

        # 开始加载
        while self.loop:
            # 保证pages中只有不超过两个元素，删除刚才显示的那一条段子
            if self.pages:
                # nowPage内有所有的段子
                nowPage = self.pages[0]
                # 删除第一条，存入下一条
                del self.pages[0]
                self.showPage(nowPage, page)
                page += 1


# 爬虫开始
print(u"""
-----------------浏览糗事百科的段子--------------
    按下任意键继续
    退出请输入"exit"
    时间:2016.5.1
    语言:python 2.7
    包:BS,RE,URLLIB2,TIME,THREAD
------------------------------------------------
"""
 )
print(
u"按下回车浏览今日糗百热门内容:")
input('>')
if __name__ == '__main__':
    myModel = spider()
    myModel.start()
