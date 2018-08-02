g = (x * x for x in range(10))
for n in g:
    print(n)

l=(x * x for x in range(100000000000000000000000000000000000000000))
print(next(l))
for n in l:
    print(n)