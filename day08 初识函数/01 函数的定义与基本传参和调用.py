# -*- coding:utf-8 -*-

def hanshu():                               #函数可以有返回值也可以没有返回值,返回的是none
    print 111

hanshu()


def hanshu2():
    print 111
    return 222
    print 333                              #凡是执行return后,后面的就不再执行了,也就是后面的333不输出
print hanshu2()
a=hanshu2()
print a



def func(canshu1,canshu2):
    print("canshu1是%s" %canshu1)
    print("canshu2是%s" %canshu2)
func(1,2)                                  #位置参数
func(canshu2=3,canshu1=4)                  #指定参数
func(5,canshu2=6)                          #混合参数,注意只有在位置参数都写完后才能写指定参数(不然就报错)



def func1(canshu1,canshu2=7):               #默认的参数,默认值也必须都写在后面,也就是说所有的等号参数都写在后面
    print canshu1,canshu2
func1(3)                                    #当缺参数的时候就用默认的参数
func1(6,8)


 # def func2(canshu1,canshu2=2,canshu3):                   #问题代码,默认参数的赋值和指定参数的赋值必须写在最后面
 #    print canshu1,canshu2,canshu3
# func2(1,,3)
 #func2(canshu1=2,3,4)
