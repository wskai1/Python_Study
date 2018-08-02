import re
import socket
import ssl
import urllib.request
from urllib import parse

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'fyonecardgwpre.cdwit120.com',
    'Referer': 'https://fyonecardpre.cdwit120.com/pregnantbaby',
    'Content-Type': 'application/x-www-form-urlencoded'
}
request = urllib.request.Request("https://fyonecardpre.cdwit120.com/pregnantbaby")
try:
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
except urllib.request.URLError as e:
    print(e)
    print(e.code)
    print(e.reason)

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

response = urllib.request.urlopen('https://www.python.org')
print(type(response))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'zhaofan'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

# ip 代理
print('IP代理')
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:80',
#     'https': 'https://127.0.0.1:80'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('https://www.baidu.com')
# print(response.read())


print("COOKIE")
import http.cookiejar, urllib.request

filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print("使用cookie")
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
pattern = re.compile('<a href.*?\"(.*?)\".*?>(.*?)</a>', re.S)
items = re.findall(pattern, response.read().decode('utf-8'))
print("items", end="")
for item in items:
    print(item)

# pattern = re.compile('<div.*?u1.*?<a href(.*?)name.*?mnav.*?>(\w+).*?</div>', re.S)
# items = re.findall(pattern, response.read().decode('utf-8'))
# print("items",end="")
# print(items)

import http.cookiejar, urllib.request

filename = 'cookie1.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
