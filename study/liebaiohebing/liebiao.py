l1=['a','b','c','d','e','f']
l2=['','我们',2,3,4,5,'d','e','f']


print(len(l1))
print(len(l2))
for i in range(len(l1)):
    for j in range(len(l2)):
        if l2[j]==l1[i]:
           print(l2[j])

print(l1+l2)
#去除列表中重复的元素 缺点：变为无序的
print(list(set(l1+l2)))

#基本满足合并两个列表 去掉重复元素 不改变排序的要求
l3=[]
for i in l1+l2:
  if i not  in l3:
    l3.append(i)
print (l3)
