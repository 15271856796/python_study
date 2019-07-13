

#所有带 'b' 的操作都是对于不是文本的操作,比如图片,音乐等等,只要不是对于汉字的操作就行

f=open("c:/tupian.jpg",mode="rb")
g=open("c:/tupian2.jpg",mode="wb")
for line in f:
    g.write(line)
f.close()
g.close()