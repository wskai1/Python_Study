stu1={'name':'张三','score':'98'}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(stu1)


class animal:
    '动物类'
    def __init__(self,species,age):
        self.species=species
        self.age=age
    def anm(self):
        print("我是"+self.species+",今年"+self.age+"岁") # python 中使用 + 进行字符串连接的操作效率低下，
        # 是因为python中字符串是不可变的类型，使用 + 连接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，
        # 当连续相加的字符串很多时(a+b+c+d+e+f+...) ，效率低下就是必然的了
        print("我是%s,今年%s岁"%(self.species,self.age))
        print("我是%(species)s,今年%(age)s岁." % {'species':'是',"age":'10'})
        print(''.join(["我是" + self.species + ",今年" + self.age + "岁"])) #使用join
        #使用 format
        str = 'There are {}, {} years old'
        print(str.format(self.species, self.age))
        str = 'There are {1}, {0} years old'
        print(str.format(self.age, self.species))
        # 使用
animal1=animal('大熊猫','10')
animal1.anm()

#面向对象
class Student:
    '学生类'
    def __init__(self,name,sex,score):
        self.name=name
        self.sex=sex
        self.score=score
    def print_stu(self):
        print("Name : ",self.name, ", Sex: ", self.sex,",Score:",self.score)

stu2=Student('张三','男','100')
stu2.print_stu()
stu3=Student('','','')
stu3.name="meokey"
stu3.score="100"
stu3.sex='女'
stu3.print_stu()


# s属性私有
class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def getname(self):
        return self.__name
    def getscore(self):
        return self.__score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
stu4=Student1('张三','55')
print(stu4.getname())
print(stu4.getscore())
stu4.set_name("王五")
print(stu4.getname())
#以下 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
stu4._name="孙六"
print(stu4._name)
print(stu4._Student1__name)
print(stu4.getname())

#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
#判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(dog,Animal))
print(isinstance(dog,Dog))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Cat())

#字符类型和长度
print(type(123))
print(type('123'))
print(type(None))
print(type(Cat))
print(len('a555'))
print('a555'.__len__())

#自己所写的类的_len_()方法
class MyDog(object):
  def __len__(self):
        return 1000
dog=MyDog()
print(len(dog))

#字符转化为小写
print('ABC'.lower())

#操作对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y)
# getattr(obj, 'z') # 获取属性'z'  如果试图获取不存在的属性，会抛出AttributeError的错误：
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
print(hasattr(obj, 'power') )# 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn)
print(fn())
print(dir(MyObject))

#由于Python是动态语言，根据类创建的实例可以任意绑定属性
class Student():
    def __init__(self,name):
        self.name=name
s=Student('OB')
s.score='90'
print(s.name+""+s.score)
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
class stu():
    name='Stuent'
s1=stu()
print(s1.name)   # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(stu.name)#打印类的name属性
s1.name = 'Michael' # 给实例绑定name属性
print(s1.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(stu.name)  # 但是类属性并未消失，用Student.name仍然可以访问
del s1.name # 如果删除实例的name属性
print(s1.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
