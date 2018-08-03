import heapq
from collections import deque

p=(4,5,6)
x,y,z=p
print(x,y,z)
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares, price)
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)

# 利用分割法实现递归
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

# 保留后几位
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
# 不定义大小的deque
p=deque()
p.append(1)
p.append(2)
p.append(3)
print(p)
p.appendleft(4)
print(p)
p.popleft()
print(p)

# 获取最大或者最小的N个数的集合
print("获取最大或者最小的N个数的集合")
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(5, nums)) # Prints [-4, 1, 2]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

nums = (1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2)
heap=list(nums)
print(heap)
heapq.heapify(heap)
print(heap)
# 堆数组最小的三位 堆数组最小的永远是heap[0]
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
if __name__ == '__main__':
    grades=[10,11,12,13,14,15,16,89,17,18,19,20,12]
    s=sorted(grades,reverse=True)[:5]
    print(s)
    print(grades)
    print(drop_first_last(grades))
    print()