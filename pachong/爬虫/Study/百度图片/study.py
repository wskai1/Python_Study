
import requests
import os
#这个url是图片，视频的路径
url = 'https://avatar.csdn.net/3/5/A/3_ling_mochen.jpg'
#root是指定的文件存储的目录
root = 'E:/wsk/Python/pachong/爬虫/Study/百度图片/图片/'
path = root + url.split('/')[-1]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print("失败了")