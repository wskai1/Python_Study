import urllib.request

req = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(req)
except urllib.request.HTTPError as e:
    print (e.code)
except urllib.request.URLError as e:
    print (e.reason)
else:
    print ("OK")