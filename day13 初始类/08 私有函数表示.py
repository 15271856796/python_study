# -*- coding:utf-8 -*-



class Fun:
    def __init__(self,name,age):
        self.name=name
        self.__age=age                                #两个下划线在前面,这个属性就是私有的
    def funa(self):
        print 1
    def __yue(self):
        print 2

fun=Fun()
#fun.__yue()                                               #不能在外面进行访问
