try:
    file=open('ee','r+')
except Exception as e:
    print('there is no file named as ee')
    response=input('do you want to create a new file?')
    if response=='y':
        file=open('ee','w')
    else:
        pass
else:                               #没有错误的时候才会执行这里的else
    file.write('hahahaha')
file.close()