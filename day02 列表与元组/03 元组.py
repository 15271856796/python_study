# -*- coding:utf-8 -*-

#元组和列表一样,只不过他是只读的数据元素


#元组的索引与切片
tip=(1,2,3,3,4,5)
print tip[2]
print tip[3:5]                                    #元组的索引与切片用法和字符串的一样

tip=tuple()
print type(tip)
tip1 =()
print type(tip1)

tip2=(1)
print type(tip2)
tip3=(1,)
print type(tip3)