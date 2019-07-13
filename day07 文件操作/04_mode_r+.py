# -*- coding:utf-8 -*-


f=open("aa4.txt",mode='r+')            #r+是先读,然后再写,并且是写在文件的尾部,必须是先读再写
print f.read(2)
f.write("何睿何睿何睿")
f.flush()                             #刷新管道,把内容写进去
f.close()
