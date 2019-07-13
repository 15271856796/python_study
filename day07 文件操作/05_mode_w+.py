# -*- coding:utf-8 -*-

f=open("aa5.txt",mode='w+')             #w+总是先写,写的时候会先进行清空,然后再读
f.write('hhh')
f.write("何睿何睿何睿")
f.flush()                               #刷新管道,把内容写进去
print f.read()                          #此时f在文本的最后面,所以导致读不到任何东西
f.seek(0)                               #句柄回到句首
print f.read()                          #此时才会有数据

f.close()