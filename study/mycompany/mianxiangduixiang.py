from types import MethodType


class Student(object):
    pass
s1=Student()
s1.name='张三'
print(s1.name)
def set_age(self, age): # 定义一个函数作为实例方法
  self.age = age
def sex(self,sex):
    self.sex=sex
s1.set_age = MethodType(set_age, s1) # 给实例绑定一个方法
s1.sex=MethodType(sex,s1)
s1.set_age(25) # 调用实例方法
s1.sex('男')
print(s1.age)
print(s1.sex)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2=Student()
#s2.sex('nv')
#为了给所有实例都绑定方法，可以给class绑定方法：
def score(self,sco):
    self.score=sco
Student.score=score
s2.score('100')
print(s2.score)

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。使用__slots__
class Student1(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
s = Student1() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
#  s.score = 99 绑定属性'score' 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student2()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
#s.score = 9999

class Student3(object):
    @property
    def birth(self):
        return  self._birth
    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._birth = value

s3=Student3()
#s3.birth='skx'
#s3.birth=120
s3.birth=10
print(s3.birth)

#多继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
            pass
class Bat(Mammal, Flyable):
    pass

# 学习定制类
class Student4(object):
     def __init__(self, name):
        self.name = name
     def __str__(self):
       return 'Student object (name: %s)' % self.name
print(Student4('李四'))