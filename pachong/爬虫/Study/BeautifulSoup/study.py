import re

import bs4
import requests
from bs4 import BeautifulSoup

response  = requests.get("https://www.baidu.com")
html=response.content.decode("utf-8")

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
# 只能查询到第一个符合条件的tag
print(soup.head)
print (soup.body.attrs)
print(soup.a)

# 获取tag的class属性
print (soup.a['class'])
print (soup.a.get('class'))
print (soup.a.get('value'))
# 修改属性
soup.a['class']="newClass"
print(soup.a)
del soup.a['class']
print(soup.a)

print(soup.a.string)

if type(soup.a.string)==bs4.element.Comment:
    print (soup.a.string)

# 获取所有子节点
print(soup.body.contents )
print(soup.body.children )
# 获取指定序号的子节点
print(soup.body.contents[1] )

tag=soup.find_all("div", attrs={"id":"u1"})
for tag in tag:
    print("获取到了这个DIV")
    print(tag)
    for s in tag.strings:
        print(s)
        # 消除多余空白
    for s in tag.stripped_strings:
        print(s)

# 条件匹配
tag1=soup.find_all("a", class_="mnav")
for tag in tag1:
    print(tag)
tag2=soup.find_all("a", attrs={"class": "mnav"})
for tag in tag2:
    print(tag)

# 查找所有A标签
print(soup.find_all('a'))
for s in soup.find_all('a'):
    print(s.string,end="")
    print(s.get('href'))

# 利用正则匹配
for tag in soup.find_all(re.compile("^d")):
    print(tag.name,end="")
    for text in tag.stripped_strings:
        print(text)


# 返回页面上所有的节点
for tag in soup.find_all(True):
    print(tag.name)


list=soup.find_all("a", class_="mnav")
for l in list:
    print(l)

# tag 属性不能搜索时候
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(da="value")

# 或者
data_soup.find_all(attrs={"data-foo": "value"})

# 限制搜索个数
soup.find_all("a", limit=2)

# 通过标签查找
print(soup.select('title'))
# 通过类
print (soup.select('.sister'))
# 通过ID
print (soup.select('#link1'))
# 组合查找
print(soup.select('a[class="sister"]'))