# -*- coding:utf-8 -*-

#类对实例变量的封装除了可以通过__init__(self)函数,也可以是通过将方法转化成变量这种方法@property

#主要用于属性的值需要通过计算才能得到


#方法一
class Fun:
    def __init__(self,name,ti):
        self.name=name
        self.ti=ti
        self.age=self.ti+9                                  #这个属性的值是通过ti这个属性的值得到的
fun=Fun('12',12)
print fun.age

#方法二

class Fun:
    def __init__(self,name,ti):
        self.name=name
        self.ti=ti


    @property                                               #加@property的作用是把函数转换成属性,属性名是函数名,属性值是函数返回值,之后直接就对象点属性,它是紧跟着初始函数后进行执行
    def age(self):
        return self.ti+9
fun=Fun('12',12)
print fun.age                                              #后面就直接当做函数不存在了,就多了个属性,在fun.age()调用的话,会报错







