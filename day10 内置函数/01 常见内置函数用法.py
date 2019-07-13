# -*- coding:utf-8 -*-

print(bin(5))                          #0b101  化成二进制
print(oct(8))                          #0c10   化成八进制
print(hex(17))                         #0x11   化成十六进制

print sum([1,2,3,4,5])
print min([1,2,3,4,5])                 #要求参数是课迭代的
print max([1,2,3,4,5])

print divmod(10,3)                     #计算商和余数 ,输出(3,1)

print abs(-3)                          #求绝对值


print round(2.5)                       #取整,四舍五入


print pow(2,3)                         #相当与2**3


list1=[1,2,3,4,5]
for index,values in enumerate(list1):  #enumerate是获取元素和索引,一个个的组成元组
    print index,values


print  all([1,2,0])                    #输出的是False,all()函数作用是判断元组中的元素是否是全部都是非零的
print  any([1,2,0])                    #输出的是True,相当于or的用法





def  func(el):
    return len(el)
s=sorted(['dhshdffs','as','dsf'],key=func)         #用规则进行进行排序
print s



list=[1,2,3,4]
r= reversed(list)                         #reversed函数的作用是反转
for el in r:
    print el

