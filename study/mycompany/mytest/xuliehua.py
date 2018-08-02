import pickle

stu = dict(name='Bob', age=20, score=88)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
str=pickle.dumps(stu)
print(str)
f = open('dump.txt', 'wb')
pickle.dump(str, f)
f.close()

f1 = open('dump.txt', 'rb')
dat = pickle.load(f1)
f1.close()
print('dat')
print(dat)

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)
reborn = pickle.loads(data)
print(reborn)