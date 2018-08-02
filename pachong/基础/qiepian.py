import os

L = list(range(100))
print(L)
print(L[1:2])
print(L[50:])

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')] )