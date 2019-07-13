# -*- coding:utf-8 -*-

# from urllib import urlopen
# def func():
#      content=urlopen("http://www.dytt8.net/").read()
#      return content.decode("gbk")
# print(func())
# print(func())




#改良版(可以多次获取content内容,而不用再链接)

from urllib import urlopen
def func1():
    content = urlopen("http://www.dytt8.net/").read()
    def inner():
        return content.decode("gbk")
    return inner


ret=func1()
print(ret())
print(ret())