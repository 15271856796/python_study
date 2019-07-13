# -*- coding:utf-8 -*-

a=10                                    #全局变量

def  func():
    print("输出里面的%s" %a)                           #可以直接引用全局的变量,前提是不对全局变量进行修改,
func()
print("输出外面的%s" %a)









a=10                                    #全局变量     自定义函数里可以直接应用全局变量,但是不允许进行修改,除非加一句声明,global a

def  func():
    global a                            #global   是指直接引用的是全局的,在要对全局变量进行修改的时候,必须加一个global
    a=a+10
    print("输出里面的%s" %a)
func()
print("输出外面的%s" %a)




b =10                                  #全局变量     自定义函数里可以直接应用全局变量,但是不允许进行修改,除非加一句声明,global a

def  func1():
    b=10
    def func2():
        global b                         #global 是指直接引用的是全局的   nonlocal 是指引用局部的,一层层的找距离最近的,但是不能找全局的
        b=b+10
        print("输出里面的%s" %b)
    func2()
    print("输出func1的b%s" %b)


func1()
print("输出外面的b%s" %b)

