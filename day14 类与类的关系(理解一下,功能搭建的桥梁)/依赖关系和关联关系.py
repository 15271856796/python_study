# -*- coding:utf-8 -*-

#事物都是有联系的,类与类之间也是
#依赖关系是指类中的函数的参数是另一个类的对象,示列如下:

class Fun:
    def pao(self,fun1):
        fun1.pao1()
class Fun1:
    def pao1(self):
        print 1111

fun=Fun()
fun1=Fun1()
fun.pao(fun1)



#关联关系是指类的初始化函数中的参数必须另一个类的对象

class Fun:
    def __init__(self,fun1):
        self.obj=fun1
    def mothod(self):
        print self.obj.name
class Fun1:
    def __init__(self,name):
        self.name=name

fun1=Fun1("hdl")
fun=Fun(fun1)
fun.mothod()
