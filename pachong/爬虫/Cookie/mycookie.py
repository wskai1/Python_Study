import urllib.request
import  http.cookiejar

# cookie保存的文件名
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie
cookie =  http.cookiejar.MozillaCookieJar(filename)
# 创建opener用于读取Url
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# 登录的用户名密码
values = {"username": "1767340368", "password": "xxxxxxxx"}
# 模拟登录
postdata = urllib.request.urlencode(values)
# 登录的Url
loginUrl = "http://home.51cto.com/index?reback=http://www.51cto.com/"
# 登录
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址
gradeUrl = "http://blog.51cto.com/1767340368"
result = opener.open(gradeUrl)
print(result.read())
