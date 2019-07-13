# -*- coding:utf-8 -*-

class Fun:
    pass
class Fun1(Fun):
    pass

fun=Fun()
fun1=Fun1()

print isinstance(fun,Fun)       #True  判断一个对象是否是某个类型的对象
print issubclass(Fun1,Fun)      #True  判断某个类是否是另一个类的子类
print type(fun)



#常见应用

def func(a,b):
    if type(a)==int and type(b)==int:
        return a+b
    else:
        print "不是两个"