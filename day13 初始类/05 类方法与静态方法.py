
# -*- coding:utf-8 -*-

class Fun1:
    def __init__(self):
        pass
    @classmethod
    def mothid(cls):                                  #这个就是类方法,可以用类名进行调用
        pass
    @staticmethod
    def static():                                     #静态方法就和我们在外面定义的函数是一样的,不像变量函数需要self,不像类函数需要cls,他就和一般的函数一样的,
                                                      #可以用类调用,也可以用对象调用,但是提倡是用类名去调用
        print '1111'
fun=Fun1()
print fun.shenggao
print Fun1.shenggao
Fun1.shenggao=10                                     #不能用对象进行修改,必须用类名
print fun.shenggao
Fun1.static()