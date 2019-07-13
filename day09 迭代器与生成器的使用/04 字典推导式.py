
# -*- coding:utf-8 -*-

# 和列表的差不多,但是差别在于放在列表中的元素形式不同,其余的for 和 if 一样

# 1 把列表中的元素变成{1:11,2:22,3:33}
list=[11,22,33]
dit={i :list[i] for i in range(len(list))}
print dit
