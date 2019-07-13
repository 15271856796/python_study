# -*- coding:utf-8 -*-

#实例变量是指必须用对象去调用的变量
class Fun:
    def __init__(self,name,tizhong):
        self.name=name
        self.tizhong=tizhong

fun=Fun('huangdeli','90')
print fun.name                                       #name和tizhong就是实例变量,必须需要实例化的对象去调用


#类变量和类函数

class Fun1:
    shenggao=100                 #在初始化函数外定义的就是类变量,类变量一般用类名去调用,对象也可以去调用,,但是不能进行修改
    def __init__(self):
        pass
    @classmethod
    def mothid(cls):              #这个就是类方法,可以用类名进行调用
        pass
fun=Fun1()
print fun.shenggao
print Fun1.shenggao
Fun1.shenggao=10                                     #不能用对象进行修改,必须用类名
print fun.shenggao