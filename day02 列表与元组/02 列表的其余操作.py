# -*- coding:utf-8 -*-

lis=[['1',2,3],[232,"dsferfr"],[1,'efr']]
print lis[1][1][3]                                      #输出的是'e'


print lis.count(['1',2,3])               #列表中某元素的计数
print lis.sort()                         #默认是升序排序
print lis.sort(reverse=True)             #降序
print lis.reverse()                      #列表里所有元素反转  从[1,2,3,4] 变成[4,3,2,1]
print len(lis)                           #列表的长度

