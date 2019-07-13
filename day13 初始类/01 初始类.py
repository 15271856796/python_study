# -*- coding:utf-8 -*-


class Car:     #类名严格遵守驼峰规则
    def __init__(self,color,paizhao):                               #当这个类没有需要封装的属性的时候可以不需要初始化函数
        self.color=color
        self.paizhao=paizhao
        print self.color,self.paizhao
    def pao(self):
        print("我是%s" %self.color)



car=Car("红色","1293894")
car.pao()


car1=Car("黑色","23243235")
car1.pao()