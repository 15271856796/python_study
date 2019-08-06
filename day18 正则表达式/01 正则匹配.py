import re  #导入正则表达式的库

#简单的Python匹配
pattern1='cat'
pattern2='bird'
string='dog runs to cat'
print(pattern1 in string)    #True
print(pattern2 in string)    #False


#用正则匹配
pattern1='cat'
pattern2='bird'
string='dog runs to cat'
print(re.search(pattern1,string))       #<re.Match object; span=(12, 15), match='cat'>
print(re.search(pattern2,string))       #None

#用正则匹配多种可能 使用[]([]中的一个),下面的例子是匹配run或者ran
ptn=r'r[ua]n'                           #不加r的话就变成了ptn='r[un]n'此时是一个表达式,加一个 r 代表这是一个表达式的意思
print(re.search(ptn,'dog runs to cat'))     #<re.Match object; span=(4, 7), match='run'>
print(re.search(r'r[ua]n','run ran ren'))   #<re.Match object; span=(0, 3), match='run'>  re.search只会匹配到第一个


#匹配多种可能,可能性不想一一列举的时候(但是只能取一个)
print(re.search(r'r[A-Z]n','dog runs to cat'))
print(re.search(r'r[A-Z0-9]n','dog runs to cat'))

#匹配数字的通配符(\d是指数字中的任意一个,\D代表不是数字中的任意一个)
print(re.search(r'r\dn','run r44n'))         #none,因为这是两个4,如果是一个4的话就可以匹配的上
print(re.search(r'r\dn','run r4n'))          #match='r4n'
print(re.search(r'r\Dn','run r4n'))          #<re.Match object; span=(0, 3), match='run'>

#匹配空白符(匹配特殊字符)中的任意一个
#\s:any white sapce [\t\n\r\f\v]
print(re.search(r'r\sn','r\nn r4n'))        #<re.Match object; span=(0, 3), match='r\nn'>
#\S:opposite to \s,any non-white space
print(re.search(r'r\Sn','r\nn r4n'))        #<re.Match object; span=(4, 7), match='r4n'>

#所有的字母数字和下划线中的任一个
#\w:[a-zA-Z0-9_]
print(re.search(r'r\wn','r\nn r4n'))        #<re.Match object; span=(4, 7), match='r4n'>
#\W:opposite to w
print(re.search(r'r\Wn','r\nn r4ns'))        #<re.Match object; span=(0, 3), match='r\nn'>

#空字符
#\b : empty string(only at the start or end of the word,only)  \b代表前后必须要有空白字符,\B代表不管前后有没有空白字符都可以
print(re.search(r'\brun\b','dog run to cat'))       #<re.Match object; span=(4, 7), match='run'>
print(re.search(r'\brun\b','dog  run  to cat'))     #<re.Match object; span=(5, 8), match='run'>
#\B:empty string(but not at the start or end of a word)
print(re.search(r"\B runs \B",'dog  runs  to cat')) #<re.Match object; span=(4, 10), match=' runs '>白


# \ 特殊字符
# \\:match \
print(re.search(r'runs\\','runs\ to me'))       #<re.Match object; span=(0, 5), match='runs\\'>

#任意字符
# . :match anything (except \n)
print(re.search(r'r.n','r-ns to me'))           #<re.Match object; span=(0, 3), match='r-n'>
print(re.search(r'r.n','r4ns to me'))           #<re.Match object; span=(0, 3), match='r4n'>

#句首句尾
# ^:match line begining
print(re.search(r'^dog','dog runs to cat'))     #<re.Match object; span=(0, 3), match='dog'>
# $ : match line ending
print(re.search(r"cat$",'dog runs to cat'))     #<re.Match object; span=(12, 15), match='cat'>
print(re.search(r"cat$",'dog runs to cat  '))   #None

#多种匹配
# ? : may or may not occur
print(re.search(r'Mon(day)?','Monday'))         #<re.Match object; span=(0, 6), match='Monday'>
print(re.search(r'Mon(day)?','Mon'))            #<re.Match object; span=(0, 3), match='Mon'>

#多行匹配
# muli-line 将文本中的每一行都看作是独立的一行
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I",string))              #None
print(re.search(r'^I',string,flags=re.M))   #<re.Match object; span=(18, 19), match='I'>

#0或者多次
# * ：occur 0 or more times
print(re.search(r'ab*','a'))                #<re.Match object; span=(0, 1), match='a'>
print(re.search(r'ab*','abbbb'))            #<re.Match object; span=(0, 5), match='abbbb'>

#1次或者多次

# + : occur 1 or more times
print(re.search(r'ab+','a'))                #None
print(re.search(r'ab+','abbbbb'))           #<re.Match object; span=(0, 6), match='abbbbb'>

#可选次数
# {n,m}:occur n to m times
print(re.search(r'ab{2,10}','a'))           #None
print(re.search(r'ab{2,10}','abbbbb'))      #<re.Match object; span=(0, 6), match='abbbbb'>

#group组
# group 用(),用()是为了分组,这样你可以取每个组所得到的匹配结果,所以带不带()完全看你自己的需求
match = re.search(r'(\d+),Date(.+)','ID:021523,Date:Feb/12/2017')
print(match.group())                    #021523,Date:Feb/12/2017
print(match.group(1))                   #021523
print(match.group(2))                   #:Feb/12/2017

#给组命名,当组多的时候,比如上百个,那么用索引取的时候都不知道哪个是哪个,所以用 ?P<组名> 给组起名字
match = re.search(r'(?P<id>\d+),Date(?P<hh>.+)','ID:021523,Date:Feb/12/2017')
print(match.group())                    #021523,Date:Feb/12/2017
print(match.group('id'))                   #021523
print(match.group('hh'))                   #:Feb/12/2017


#寻找所有的匹配
#findall
print(re.findall(r'r[ua]n','run ran ren'))              #['run', 'ran']
print(re.search(r'r[ua]n','run ran ren'))               #<re.Match object; span=(0, 3), match='run'>


# |:or
print(re.findall(r'run|ran','run ran ren'))             #['run', 'ran']



#compile 将表达式先分装起来
complied_re=re.compile(r"r[ua]n")
print(complied_re.search('dog ran to cat'))                 #<re.Match object; span=(4, 7), match='ran'>
