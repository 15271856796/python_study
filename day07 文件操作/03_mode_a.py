# -*- coding:utf-8 -*-


f=open("aa3.txt",mode='a')            #每次有a打开这个文件,他会自动在文件的尾部进行追加,当文件不存在时,会自动创建这个文件
f.write("何睿何睿何睿")
f.flush()                             #刷新管道,把内容写进去
f.close()
