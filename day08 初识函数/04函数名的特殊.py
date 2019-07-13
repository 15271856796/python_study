# -*- coding:utf-8 -*-

def func():
    print "func"
    return func1                           #返回的必须是真实存在的函数名,且不带单引号或者双引号
def func1():
    print "func1"
    return func
def func2():
    print "func2"
    return func2
def func3():
    print "func3"
    return func2
def fun(a):
    return a()
ret = func()
ret()                                        #函数名的特殊用法

fun(func1)



