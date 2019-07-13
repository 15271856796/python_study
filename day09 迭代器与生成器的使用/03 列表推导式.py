
# -*- coding:utf-8 -*-

# 列表推导式是有固定形式的  [要放在列表中的元素 for循环(可以有多个) if判断]

# 1 把1到100的数以我是1,这种形式放入列表中

lit =["我是%s" %i for i in range(1,101)]
print lit



# 2 把1到100中的偶数的平方放入列表中

lit1=[a**2 for a in range(1,101) if a%2==0]
print lit1

# 3 把下列列表中有两个'e'的元素挑出来

list=[["fesd","efged"],["sadsa","dseeda"]]

lit2=[l for el in list for l in el if l.count("e")>=2]
print lit2


#可以先写循环,再写判断,然后再写列表中要有的元素