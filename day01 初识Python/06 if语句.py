# -*- coding:utf-8 -*-

money = input("请输入你的钱;")
if money>200:
    print("吃烧烤")                              #直接一个tab就可以手动进行缩进
    print("吃火锅")
    if money >300:                                #多重的嵌套
        print("吃自助")
    else:
        print("吃麻辣烫")
    print("哈哈哈哈")
elif money>100:
    print("吃盖饭")
elif money==90:
    print("吃泡面")
else:
    print("啥也不吃")