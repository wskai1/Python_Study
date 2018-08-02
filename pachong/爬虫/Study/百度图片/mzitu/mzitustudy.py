import re
import string

import requests
from bs4 import BeautifulSoup
import os

file_ph = 'E:\wsk\Python\pachong\爬虫\Study\百度图片\mzitu'
class mzitu():
    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
    def all_url(self, url):
        html = self.request(url)##调用request函数把套图地址传进去会返回给我们一个response
        for ul in BeautifulSoup(html.text, 'lxml').find_all('ul',class_='archives'):
            year=ul.previous_sibling.get_text()
            # 外层目录
            lis = ul.find_all('li')
            for index,li in enumerate(lis):
                mk_outer_dir=li.find('p')
                title = mk_outer_dir.get_text()
                self.mkdir(year+title)
                global file_ph
                file_ph=file_ph+r'/'+year+title
                # 内层目录
                mk_inner_dir=li.find_all('a')
                for lj in mk_inner_dir:
                    text = re.sub("[:？?]","",lj.get_text())
                    self.mkdir(text)
                    href=lj['href']
                    self.html(file_ph+r'/'+text+r'/',href)
                file_ph='E:/wsk/Python/pachong/爬虫/Study/百度图片/mzitu'
            # href = a['href']
            # self.html(href) ##调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！

    def html(self,path, href):   ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(href)
        self.headers['referer'] = href
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(path,page_url) ##调用img函数

    def img(self,path, page_url): ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(path,img_url)

    def save(self,path, img_url): ##这个函数保存图片
        name = path+img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path): ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join(file_ph, path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join(file_ph, path))
            os.chdir(os.path.join(file_ph, path)) ##切换到目录
            return True
        else:
            # print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def request(self, url,num=3): ##这个函数获取网页的response 然后返回
        try:
            content = requests.get(url, headers=self.headers,timeout = 500)
        except Exception as e:
            if num > 0:
                return  self.request(url=url, num=num - 1)
        return content
if __name__ == '__main__':
    Mzitu = mzitu() ##实例化
    Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）