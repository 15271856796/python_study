# -*- coding:utf-8 -*-

# 一for对字符串的迭代

s="hsshdjshkshdiudehd"
for i in s:
    print i


#二 for对列表的迭代
list=[1,2,3,4,5]
for i in list:
    print i


#三 for对元组的迭代
t=(1,2,3,4,6)
for i in t:
    print i

#四  for对range的遍历
lis=[1,2,3,4,5]                                     #range也只是顾头不顾尾
for i in range(1,5):
    print ("列表中的元素为%s%s" %(i,lis[i]))



#五  for对字典的遍历
dict ={"1":1,"2":2,"3":3}
for key in dict:                                       #是对字典的key进行遍历
    print key
    print dict[key]


dict.keys()
dict.values()
print(dict.items())         #得到字典中的所有的键值对 [("1",1),("2",2),("3",3)]
for item in dict.items():
    k,v = item              #python中的赋值都可以进行解包,a,b,c=[1,2,3] 或者 a,c=(1,2) 或者a,c=1,2
    print k,v




#for 对集合的遍历
sets={1,2,3,4,5,6}
for set1 in sets:
    print set1        #由于集合没有索引,也没有关键字,所以只能这种方法去遍历



#for对文件的遍历,利用文件句柄

f=open("../day07 文件操作/aa.txt",mode='r',encoding='utf-8')
for line in f:
    print line.strip()
f.close()

