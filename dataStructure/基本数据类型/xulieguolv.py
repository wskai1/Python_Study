from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
s=[n for n in mylist if n > 0]
print(s)
v=[n for n in mylist if n < 0]
print(v)

# 以上使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
# 如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。比如：
pos = (n for n in mylist if n > 0)
print(pos)
for s in pos:
    print(s,end=" ")
print()
#
# 过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来。
# 比如，假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过滤代码放到一个函数中，
# 然后使用内建的 filter() 函数。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '


addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5=[n>5 for n in counts]
print(more5)
TrueAddress= list(compress(addresses, more5))
print(TrueAddress)