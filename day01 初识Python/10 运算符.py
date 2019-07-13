# -*- coding:utf-8 -*-


a=1
b=2
c=0
if a<>b:                               #不等于的符号
    print a,b
if a!=c:                                #不等于的符号
    print a,c
if b==c:                                 #等于的符号
    print b



#    +=  -=  *=  /=  %=  //=


if a==1 and b==2:                        #and  or   not的用法
    print 12
if b==2 or c==3:
    print 23
if not c:
    print("c等于0")

print(3<2 or 4>5 and 6<1 or 3<9)        # 优先级是() not and or


print(a and b)    #and有假就停止运算,否则一直运算,这题输出的数b的值
print (c and b)   #会输出的是c的值
print(a or b)     #or是遇到真就停止,这题输出的是a的值