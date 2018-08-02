from functools import reduce


def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
t = map(str,[9,8,7,6,5,4,3,2,1,0])
print(list(t))


def add(x,y):
    return x+y
print(reduce(add,[1,2,3,7,8,9,10]))

print(sum([1,2,3,4,5,6]))

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2,3,4,5,6,7, 4, 5, 6, 9, 10, 15])))

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21],key=abs))

# 忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[-1]
L2 = sorted(L,key=by_name)
print(L2)
L3= sorted(L,key=by_score,reverse=True)
print(L3)

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f=by_score
print(f.__name__)