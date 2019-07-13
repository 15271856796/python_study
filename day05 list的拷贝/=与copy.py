# -*- coding:utf-8 -*-

list1=[1,2,3,5]
list2=list1
list1.append("6")
print list1,list2                  #都是[1,2,3,5,'6'],因为有=的时候是把地址给了list2,并没有创建新的对象,即id(list1)=id(list2)


#正确的用法是
print type(list1)
list2=list1.copy()
list1.append("hh")
print list1,list2               #此时改变list1,不会对List2有影响

