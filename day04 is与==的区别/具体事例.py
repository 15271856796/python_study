# -*- coding:utf-8 -*-

#"==" 是比较数据,而is是比对内存地址,Python中,数据,字符串,boolean值是事先存在数据缓冲池中的,所以地址是一样的

a='hggggg'
b='hggggg'

print (a is b)            # True

a=[1,2,3]
b=[1,2,3]
print (a==b)              #True
print (a is b)            #False