import chardet
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import requests
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('io.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

#其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

#比如，模糊效果也只需几行代码：
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('io.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')



#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 100 * 4
height = 100
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((100 * t + 50, 25), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
#扭曲
#image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
image.save('code.jpg', 'jpeg')
# 显示图片
image.show('code.jpg')


r = requests.get('https://www.baidu.com/') # 豆瓣首页
print(r.status_code)
print(r.text)

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print( r.content)
#requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

#需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)
#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})

#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post("https://www.douban.com/search", json=params) # 内部自动序列化为JSON
#类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post("", files=upload_files)
#requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
print( r.cookies['ts'])
#要在请求中传入Cookie，只需准备一个dict传入cookies参数：
cs = {'token': '12345', 'status': 'working'}
r = requests.get("url", cookies=cs)
