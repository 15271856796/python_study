# -*- coding:utf-8 -*-

#函数中包含了yield,此函数就是生成器函数
#大坑: 生成器函数运行之后是产生一个生成器,而不是运行函数,想运行函数的话是next(),或者send()

def func():
    print 11
    yield 1                              #yield的作用和return一样,两者的区别是函数执行到return时就结束,但是执行到yield也有返回值但是不会结束
    print 22
    yield 2
    print 33
    yield 3
    print 44

ret = func()

a=ret.next()                               #只会执行到第一个yield,输出了11且a=1
b=ret.next()                              #执行从第一个yield执行到第二个yield,输出22,且b=22 ,
a=ret.next()
ret.next()                                #这里会报错,因为没有yield,所以应该加一个try,except




def func1():
    print 11
    a = yield 1                             #yield的作用和return一样,两者的区别是函数执行到return时就结束,但是执行到yield也有返回值但是不会结束
    print(a)

    b=yield 2
    print("b", b)

    c=yield 3
    print("c",c)


ret = func1()

a=ret.next()
b=ret.send(22)                               #send()和next的功能一样,区别在于send可以给上一个yield进行赋值,本例中如果用next的话,a,b,c的值都是none
a=ret.send(33)







