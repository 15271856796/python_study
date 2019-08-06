
# -*- coding:utf-8 -*-

#注意集合是没有索引和切片的(因为集合是无序的)

#集合就是字典中的key,所以里面元素是不能重复

#set的常用是对列表中的元素进行去重
lis=[1,2,1,3,5,123,5]
lis=set(lis)
print(lis)                  #{1, 2, 3, 5, 123}



#set还有一个常用功能是元素分解(分解并去重)
sentence='Welcome Back to This Tutorial'
print(set(sentence))        #{'l', 'h', 'e', 'm', 'W', 's', 'o', 'u', 'a', 'c', ' ', 'k', 'T', 't', 'i', 'B', 'r'}



#set集合的添加元素
sets={1,2,4,6,7}
sets.add("1")
print(sets)             #{1, 2, '1', 4, 6, 7}


#set集合的删除元素
set3={1,2,3,4,5,'1'}
set3.pop()                          #随机的删除一个元素
set3.remove('1')                    #指定删除一个
print(set3)                         #{2, 3, 4, 5}



#删除集合中没有元素,不想让他报错的方法,用remove的话会报错
set1={1,23,'p',90}
set1.discard('h')



#set的清空
set_unique={1,2,3,4}
set_unique.clear()
print(set_unique)           #set()


#集合的修改
#由于集合即没有索引,又没有关键词,所以不能修改,只能是要把修改的东西珊掉,再重新的加一个


#两个集合之间的运算
set1={1,2,3,4}
set2={3,4,5}
print(set1.difference(set2))                #{1, 2},找set1中有,set2中没有的
print(set1.intersection(set2))              #{3, 4},找set1和set2中都有的

#集合的查询

for setitem in sets:
    print(setitem)




