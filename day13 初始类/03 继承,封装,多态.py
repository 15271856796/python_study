# -*- coding:utf-8 -*-


   #封装的含义就是把一类事物特有的属性和功能封装起来,可以创建多个对象,大家都有这些属性和功能

   #继承的含义是指子类可以有父类除了私有的东西



#继承基本含义

class Parent:
    def dong(self):
        print 111


class Son(Parent):                                      #括号括起来就代表是继承关系
    def pao(self):
        print 2222
    def dong(self):
        print 11111


son=Son()
son.dong()                                                #子类与父类都有同一个函数的时候,优先选择自己的,这个叫方法的覆盖和重写
son.pao()



#python支持多继承

class Food:
    def chi(self):
        print('chi')
    def La(self):
        print("lalallala")
class Food1:
    def he(self):
        print("he")
    def La(self):
        print("kkkkkkkk")


class Son(Food,Food1):                                     #多继承的表示方法,如果两个父类中有同样的函数,就近原则,所以调用的是Food的,近的是亲爹,远的是干爹
    def __init__(self):
        pass
son=Son()
son.chi()
son.he()
son.La()                                                   #也是就近原则,所以调用的是Food的La()



#多态是指一个父类的多个子类的对象可以有不同的形态.可以都对父类的方法进行改写.
