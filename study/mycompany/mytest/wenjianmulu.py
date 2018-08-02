import os
print(os.name) # 操作系统类型
#print(os.uname())# windows 不提供该函数
print(os.environ)
print(os.environ.get('PATH'))
# 列出当前目录下的所有目录
print( [x for x in os.listdir('.') if os.path.isdir(x)])
#列出当前目录下的所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


