import json

import requests
import urllib3
from requests import ReadTimeout, RequestException
from requests.auth import HTTPBasicAuth

response  = requests.get("https://www.baidu.com")
print("response类型：",end="")
print(type(response))
print("response状态码：",end="")
print(response.status_code)
print(type(response.text))
print("网页源代码")
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))

# 各种请求
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")

# get请求
response = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response.text)
import requests
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)


# 解析JSON
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

# 直接访问知乎
response =requests.get("https://www.zhihu.com")
print(response.text)
# 带headers访问知乎
import requests
headers = {

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response =requests.get("https://www.zhihu.com",headers=headers)

print(response.text)


# POST请求
data = {
    "name":"zhaofan",
    "age":23
}
response = requests.post("http://httpbin.org/post",data=data)
print(response.text)

# ssl验证

urllib3.disable_warnings()
response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)

# 代理IP
proxies= {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}
response  = requests.get("https://www.baidu.com",proxies=proxies)
print(response.text)

# 异常处理
try:
    response = requests.get("http://httpbin.org/get",timout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")

# 认证
response = requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user","123"))
print(response.status_code)
response = requests.get("http://120.27.34.24:9001/",auth=("user","123"))
print(response.status_code)