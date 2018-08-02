# f = open('/Users/michael/test.txt', 'r')  不存在的情况
f=open('io.txt','r')
s=f.read()
f.close() # 不准确 一旦程序出错 就不能执行到该语句
print(s)
print("引入try 避免文件不能关闭")
try:
    f1 = open('io.txt', 'r')
    print(f1.read())
finally:
    if f1:
        f1.close()

print("但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：")
with open('io.txt', 'r') as f2:
    print(f2.read(2))

print("前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：")
with open('io.jpg', 'rb') as f2:
    print(f2.read())

print("写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：")
with open('io.txt', 'a+') as f:
    f.write('Hello, world!\n')
with open('io.txt', 'r') as f:
    str=f.read();
    print(str)

