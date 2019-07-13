# -*- coding:utf-8 -*-

lis = ['1','wdgewgfu',[1,'wqdwd'],'9','5','2','1']                         #列表相当与一个大口袋,对里面的元素没有要求,逗号隔开就行



lis[1]                                                      #列表的索引和切片的字符串用法一样
lis[:2]                                                     #切片就和索引是一样的,只是查看的作用,没有修改列表的功能
lis[-1::-2]                                                 #[[1,'wqdwd'],'1']  倒着切






lis.append(u"何睿")                                          #lis相当与一个背包,所以会实时的改变列表的内容,和字符串是不一样的,所以这个lis就变成了["何睿"]
print lis                                                           #且都追加在list的最后

#插入的使用,list.insert(位置,内容)
lis.insert(0,"德丽")                                         #在索引为0的位置放上"德丽"




#删除
#pop(索引)
lis.pop(3)
#pop()默认删最后一个
lis.pop()
#remove(元素)
lis.remove('何睿')
#clear清空
lis.clear()



#修改列表的方法
lis[2]="哈哈哈哈"                               #直接就是列表索引重新的赋值


#查询
for i in lis:
    print i