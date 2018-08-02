# -*- coding: utf-8 -*-
from pip.cmdoptions import log

print('包含中文的str')
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hi,%s,你已经%.2f' %('bob',200))

print('growth rate: %d %%' % 7)
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

#定义一个数字的tuple和定义一个数值
t=(1,)
print(t)
t1=(1)  #同t1=1
print(t1)

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，
# 指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
print(t)
print('显示第一个元素',t[0][0])
t[2][0]='我'
t[2][1]='们'
print(t)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

s = input('birth: ')
birth=int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

try:
    ih=input('输入身高(cm):')
    h=int(ih)/100
    iw=input('输入体重(kg)：')
    w=int(iw)
    BMI=round(w/(h*h),2)
    print('您属于：')

    if BMI <18.5:
        print('體重過輕')
    elif 25>BMI>=18.5:
            print('正常範圍')
    elif 28>BMI>=25:
            print('过重')
    elif 32>BMI>=28:
            print("肥胖")
    else:
            print('严重肥胖')
except Exception as e:\
    print('except:', e)
#finally:
#    print('finally...发生了异常')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
for x in range(1,101):
    print(x,end=' ')
    if(x%10==0):
        print()
#递归实现斯洛塔
def move(n, a, b, c):
    if(n==1):
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(3,'A','B','C')

# 函数
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1)
print(f2)
print(f1())
print(f2())
print(f1==f2)

#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# map()函数
def square(x):
    return x**2
list1=map(square,[1,2,3,4,5])
print(list(list1))
list2=map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(list(list2))
list3=map(lambda x,y:x*y,[1,2,3],[4,5,6])
print(list(list3))

#遍历list
s=(1,2,3,4,5,6,7,8,9,10)
print(list(s))


#匿名函数 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
list4=map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(list4))
f4=lambda x:x**3
print(f4)
print(f4(5))
def build(x, y):
    return lambda: x * x + y * y
f5=build(1,2)
print(f5)
print(f5())

#偏函数
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))
print(int2('1010101'))
import functools
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
int3 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000',base=10))