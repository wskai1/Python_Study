import requests
from pyquery import PyQuery

response  = requests.get("https://www.baidu.com")
html=response.content.decode("utf-8")
doc = PyQuery(html)
print(doc)
print(type(doc))
print(doc('a'))

doc = PyQuery(url="http://www.baidu.com",encoding='utf-8')
print(doc('head'))
list=doc('#u1')
print(list)
print(list.find('a'))

for a in list.children():
    print(a.text)

a=doc('#u1 a')
print(a.text())