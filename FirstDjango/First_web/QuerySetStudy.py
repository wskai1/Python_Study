# #coding=UTF-8
#
#
# from FirstDjango.First_web.models import Tab1
#
# b = Tab1(name='Beatles Blog',sex='女',age='20')
# b.save()
# 总之，一共有四种方法
# # 方法 1
# Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")
#
# # 方法 2
# twz = Author(name="WeizhongTu", email="tuweizhong@163.com")
# twz.save()
#
# # 方法 3
# twz = Author()
# twz.name = "WeizhongTu"
# twz.email = "tuweizhong@163.com"
# twz.save()
#
# # 方法 4，首先尝试获取，不存在就创建，可以防止重复
# Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
# # 返回值(object, True/False)
#
#
# Person.objects.all()  # 查询所有
# Person.objects.all()[:10]
# 切片操作，获取10个人，不支持负索引，切片可以节约内存，不支持负索引，后面有相应解决办法，第7条
# Person.objects.get(name="WeizhongTu")  # 名称为 WeizhongTu 的一条，多条会报错
#
# get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
# Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
# Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
#
# Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
# Person.objects.filter(name__icontains="abc")  # 名称中包含 "abc"，且abc不区分大小写
#
# Person.objects.filter(name__regex="^abc")  # 正则表达式查询
# Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
#
# # filter是找出满足条件的，当然也有排除符合某条件的
# Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
# Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的
#
# Person.objects.filter(name__contains="abc").delete()  # 删除 名称中包含 "abc"的人
#
# 如果写成
# people = Person.objects.filter(name__contains="abc")
# people.delete()
# 效果也是一样的，Django实际只执行一条
# SQL语句。
# Person.objects.filter(name__contains="abc").update(name='xxx') # 名称中包含 "abc"的人 都改成 xxx
# Person.objects.all().delete() # 删除所有 Person 记录
#
# twz = Author.objects.get(name="WeizhongTu")
# twz.name="WeizhongTu"
# twz.email="tuweizhong@163.com"
# twz.save()  # 最后不要忘了保存！！！