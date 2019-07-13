# -*- coding:utf-8 -*-

#字典是无序的,里面的内容随机的变动,字典的key就相当与索引.一切都是基于key之上的操作

dict ={"aa":1,"bb":2,"cc":3}              #字典中没有索引的说法
print dict["aa"]



#字典的增的用法
dict["dd"]="4"                            #不是说一定加在字典的尾部
print dict


#字典的删的用法
dict.pop("dd")
print dict
# dict.clear()




#字典的改的用法

dict["aa"] =21
print dict