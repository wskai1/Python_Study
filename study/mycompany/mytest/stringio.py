from io import StringIO, BytesIO

f=StringIO()
f.write('Hello')
f.write(',')
f.write('World!!!')
print(f.getvalue())
#tell() 方法返回文件的当前位置，即文件指针当前位置。
print(f.tell())
#file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正往结束方向移动，
# 负往开始方向移动。如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
f.seek(1)
print(f.tell())
print(f.readline())
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
  s = f.readline()
  if s == '':
       break
  print(s.strip())
print(f.tell())
print("\n")
f.write('把以前的内容覆盖了吗？')
print(f.getvalue())

# 这样会覆盖掉第一次输入的内容，这里因为你一开始seek在0，所以你write()的时候是从0开始覆盖的。
# 如果想追加，可以使用readline()读取全部，让seek到达最后，或者使用seek(n)，手动把seek标志到最后
f1=BytesIO('中文'.encode('utf-8'))
print(f1.tell())
print(f1.readline())
f1.write('中文'.encode('utf-8'))
print(f1.tell())
f1.seek(0)
print(f1.read())