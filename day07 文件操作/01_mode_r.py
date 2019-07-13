# -*- coding:utf-8 -*-



f=open("aa1.txt",mode="r")        #f是一个光标,指向文件的最开头,当文件aa.txt不存在时,会报错
print f.read()                   #read()函数是全读,所以现在光标指向文件的最后

c2=f.read()                       #此时再读时,就是空了
print c2

#所以要养成一个好的习惯

f.close()                          #关闭f与文件的链接

f=open("aa1.txt",mode="r")
print f.read(5)                    #读5个字符
print f.read(5)                    #继续读5个字符

print f.readline()                 #以换行符分割,readline获取的时候会有一个换行,print里也是会有一个换行,为避免两个换行
print f.readline().strip()         #strip()可以去掉字符头和尾的空格,\t还有换行



#注意路径那里可以是相对路径,即从当前的文件夹开始找,也可以是绝对路径,从磁盘根目录开始找.如c盘,d盘等
#  ..是到上一文件夹,   ../..是到上两层文件夹 一个..只能返到一层的文件夹
