from collections import ChainMap
from itertools import groupby
from operator import itemgetter

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
print("相同的keys")
s = a.keys() & b.keys()
print(s)
print("a有b无的key")
print(a.keys() - b.keys())
print("相同的键值对")
v = a.items() & b.items()
print(v)

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

# 字典排序
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_name = sorted(rows, key=lambda r: r['fname'])
print(rows_by_name)

minuid = min(rows, key=itemgetter('uid'))
maxuid = max(rows, key=itemgetter('uid'))
print(minuid)
print(maxuid)

# 字典分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

    # 从字典中提取子集
prices ={
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)


# 字典合并
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c=ChainMap(a,b)
print(c)
print(len(c))
print(list(c.keys()))
print(list(c.values()))
# 如果出现重复键，那么第一次出现的映射值会被返回。 因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
# 对于字典的更新或删除操作总是影响的是列表中第一个字典
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
del c['y']