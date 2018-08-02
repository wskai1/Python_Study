def person(a, b, *, c, d=0):
    print('a =', a, 'b =', b, 'c =', c, 'd=',d)


person(1,2,c=3,d=4)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print('calc:',end='')
print(calc())
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))

# 可传入任意
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

# 只接受限制的名字的参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)
s=['1','2']
person('Jack', 24,s, city='Beijing', job='Engineer')

# 组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)