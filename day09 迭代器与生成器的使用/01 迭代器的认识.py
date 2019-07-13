# -*- coding:utf-8 -*-

#注意:是否可迭代是指是否可以for这样一个个的连续的取出
#     是否是迭代器是指是否可以一个个的间断的取出,而不用for去取值,直接next()函数就可以


list1=[1,2,3,4]
print dir(list1)
ls= list1.__iter__()                                #取list1的迭代器
while 1:
    try:
        print ls.next()                             #迭代器可以一个个的取出内容
    except:
        break



from collections import Iterable,Iterator

list1=[1,2,3,4]
print(isinstance(list1,Iterable))                     #判断是否是可迭代的
print(isinstance(list1,Iterator))                     #判断是否是迭代器
ls=list1.__iter__()
print(isinstance(ls,Iterator))


list1=[1,2,3,4]
ls=iter(list1)                 # ls是迭代器,和list.__next__()效果一直,只不过换成了用
print ls.next()
print next(ls)



for el in ls:                #也可以用for来一次性的输出迭代器和生成器里的所有内容,而不用next的这样一个个的取
    print el


