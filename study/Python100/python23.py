# -*- coding: UTF-8 -*-


from sys import stdout
from __builtin__ import raw_input
for i in range(10):
    for j in range(9-i):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print

for i in range(9):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(16 - 2 * i + 1):
        stdout.write('*')
    print


a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print (s)


s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
x = int(raw_input("请输入一个数:\n"))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10
if a != 0:
    print("5 位数："),
    print(e, d, c, b, a)
elif b != 0:
    print("4 位数：", e, d, c, b,)
elif c != 0:
    print("3 位数：", e, d, c)
elif d != 0:
    print("2 位数：", e, d)
else:
    print("1 位数：", e)

def three_hellos():
    for i in range(3):
        print("Hello Worlds")
if __name__ == '__main__':
    three_hellos()

# 输出指定范围内的素数

# 用户输入数据
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
