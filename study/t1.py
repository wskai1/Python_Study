from operator import itemgetter
print("你好啊")
print("I\'m OK")
print('\\\n\\')
print("""n = 123\nf = 456.789\ns1 = 'Hello, world'\ns2 = 'Hello, \\'Adam\\''\ns3 = 'Hello, "Bart"'\ns4 = '''Hello,\nLisa!'''""")
print("'亲爱的%s你好！你%d月的话费是%.2f，余额是%.2f."%("张三",10,230.0,120.36))
s1=72
s2=85
r=(s2-s1)/s1*100
print('hello,{0},成绩提升了 {1:.1f}%'.format('小明',r))
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

print(list(range(50)))
sum=0;
for x in range(101):
    sum+=x
print(sum)

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print( bool(1))
print(bool(''))

def my(x):
	if x>3:
		return x;
	else:
		return -x;
print(my(1))

def jiechen(n):
	if n==1:
		return 1;
	else:
		return n*jiechen(n-1);
print(jiechen(1));
print(jiechen(10));
print(jiechen(5));
print(jiechen(100));


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
L = list(range(1,101))
print(L)
print(L[5:10])
print(L[-10:])
print(L[10:50])
print(L[::4])

#map
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

#filter
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#排序
print(sorted([36, 5, -12, 9, -21]))
#绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))
#不区分大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#不区分大小写逆序排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(itemgetter(0)(L))
print(itemgetter(2,1)(L))

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]
for i in range(len(L)):
	print(by_name(L[i]))
print(sorted(L,key=by_name))

for i in range(len(L)):
	print(by_score(L[i]))

#偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
print('end')