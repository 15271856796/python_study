

#        1 整型  用于基本计算 int("10")  str(10)  bool(10)
#        2 bool型 用于判断语句
#        3字符,字符串 ①字符串的索引:从0开始,a="我是何睿,我最优秀" a[3]='睿'
#                        索引也可以倒着数,那么最后一个元素是-1,即a[-6]='睿
#                     ②切片:a[3:7]='睿,我最'   顾头不顾尾,且默认从右往左切
#                            a[-7:-2]='何睿,我最'
#                            a[7:3] 切不到任何东西
#                            a[:7]   从头开始切, a[3:]  一直切到尾
#                      ③带步长的切片:a[start:end:step]   步长表示每几个取一个
#                                     a[1:7:2]='是睿,我'
#                                     注:步长可以控制方向  a[7:3:-2]="优我"    正的步长代表是默认的从右往左切,而步长为负数的时候是从左往右切,字符串变反
#                      ④把字符串所有字母转化成大小写  f='jhdjkshduhu'    g=f.upper()   常用于项目中忽略用户输入的大小写的时候
#                                                                         g=lower()     都变成小写
#                      ⑤去掉字符串左右两端的的空白(空格,/n,/t),中间的不动  s="   da du j "   s1=s.strip()="da du j"    一般用于在用户输入用户名的时候去掉两端的空格
#                                                                                             s1=s.strip("da")         去掉字符串两端的da
#                                                                                             s1=s.lstrip()            去掉字符串左边的空格
#                                                                                             s1=s.rstrip()            去掉字符串右边的空格
#                      ⑥字符串内容的替换        s1.replace("da","ad")    s1.replace(" ","")
#                      ⑦ 字符串的切割           s2="l1_l2_l3_l2_l4"  s1.split("_l2_")=[l1,l3,l4]
#                      ⑧判断字符换的开头或者结尾        s2.startswith(l1)    s2.endswith(l3)
#                      ⑨字符串中字符个数的判断          s2.count("l")
#                      ⑩字符串的字符查找                s2.index('l2')=s2.find("l2")=4   返回的是索引,把这两个字符做整体,两个两个字符的进行比对 不同在于index()m没找到的话是会报错,find没找到的话是返回-1
#                      十一 字符串的组成判断       ①s="ashand很多很多"   s.isalpha() 为真,这个函数的意思是s必须是由字母和汉字组成,不能有标点符号等
#                                             ②s="132243464576"     s.isdight()为真,这个函数的意思是s必须是由数字组成
#                      十二 字符串的长度计算
