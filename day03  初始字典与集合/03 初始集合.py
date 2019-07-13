
# -*- coding:utf-8 -*-

#注意集合是没有索引和切片的

#集合就是字典中的key,所以里面元素是不能重复
#set的常用是对列表中的元素进行去重

lis=[1,2,1,3,5,123,5]
lis=set(lis)
print lis
lis=list(lis)
print lis



#set集合的添加元素

sets={1,2,4,6,7}
sets.add("1")
print sets

#set集合的删除元素

sets.pop()             #随机的删除一个元素
sets.remove(123)       #指定删除一个

#sets.clear()


#集合的修改
#由于集合即没有索引,又没有关键词,所以不能修改,只能是要把修改的东西珊掉,再重新的加一个



#集合的查询

for setitem in sets:
    print setitem




