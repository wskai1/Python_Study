from decimal import Decimal

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361,3))

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))
print(round(a,5))

a = 4.2
b = 2.1
sum=a+b
print(sum)
print(sum==6.3)

a = Decimal('4.3')
b = Decimal('2.1')
print(a+b)
print((a + b) == Decimal('6.4'))
print(b/a)