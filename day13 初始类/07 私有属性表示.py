# -*- coding:utf-8 -*-


#私有的属性表示

class Fun:
    __pri=20                                               #私有的类变量,只有在类里用类名点去调用
    def __init__(self,name,age):
        self.name=name
        self.__age=age                                #两个下划线在前面,这个属性就是私有的,下面访问的时候都要带上下划线
    def pri_age(self):
        print("我的名字是%s,大家的私有是%s" %(self.__age,Fun.__pri))              #类内可以随意的用私有属性

fun=Fun('hdl',18)
print fun.name                                               #name这个属性不是私有的,在类外可以进行访问
#print fun.age                                           #这个就会报错,因为age是私有的属性,只能在类内访问
fun.pri_age()


