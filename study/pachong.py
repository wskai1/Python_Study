#coding=utf-8
import meta as meta
import requests
from bs4 import BeautifulSoup

url = 'http://www.itest.info/courses' # 定义被抓取页面的url
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历页面上所有的h4
for course in soup.find_all('h4'):
    # 打印出h4的text属性
    print(course.text)


url = 'https://www.v2ex.com/'
soup1 = BeautifulSoup(requests.get(url).text, 'html.parser')
for span in soup1.find_all('span', class_='item_title'):
    a=span.find('a')
    print(a.string+"--"+a['href'])



url = 'https://www.zhihu.com/explore'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

soup = BeautifulSoup(requests.get(url,headers=headers).text, 'html.parser')

for link in soup.find_all('a', class_='question_link'):
    print(link.text)