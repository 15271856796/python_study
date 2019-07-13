# -*- coding:utf-8 -*-

#装饰器的主要功能是指在目标函数前后加入一段代码,但是不改变目标函数原来的代码

#标准装饰器的代码如下:



#首先是不要参数的简易版(不要参数的话,装饰器很有局限性,只能给不需要参数的函数进行装饰)
def wrapper(fn):                                                          #这个函数的名字是可以变的
    def inner():
        #-----加在前面的内容------
        ret = fn()
        #-------加在后面的内容------
        if ret !='none':
            return ret
    return inner
def func():
    pass
    #-----随意添加func的内容-----

func=wrapper(func)
func()                                                                   #这个时候func其实是inner




#注意这个时候func其实是没有参数的,那么如果我要对其进行传参怎么办呢??或者是对多个不同参数的函数进行装饰怎么办呢?

def wrapper(fn):
    def inner(*args,**dict):                     #传进来后args是元组,dict是字典,可以一个个的取
        #---------加在前面的内容-------
        ret=fn(*args,**dict)
        #---------加在后面的内容-------
        if ret !='none':
            return ret
    return inner


def func(a,b):
    pass
    #-----随意添加func的内容-----
def func1(c):
    pass
    #-----随意的添加func的内容-----


func=wrapper(func)
func(1,2)                                                   #这个时候func其实是inner

func1=wrapper(func1)
func1(4)

#可以发现在想用装饰器的时候,都要用类似于func=wrapper(func) 这句话,所以为了简化一般在定义目标函数的时候就这么做

@wrapper                                               #随着装饰器的名字变化而变化
def func(a,b):
    pass
    #--------随意添加func的内容-----

func(1,2)                                            #因为在定义的时候加了@wrapper,所以这里可以直接用
