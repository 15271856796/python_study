# -*- coding:utf-8 -*-

# 递归的思想在于自己调用自己,可以用于处理不停的做同样的事
def func():
    print("递归")
    func()

func()