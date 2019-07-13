
# -*- coding:utf-8 -*-


f=open("aa2.txt",mode='w')            #每次有w打开这个文件,他都会清空这个文件,然后再进行写操作,当文件不存在时,会自动创建这个文件
f.write("何睿何睿何睿")
f.flush()                             #刷新管道,把内容写进去
f.close()

