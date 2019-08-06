import pickle

#pickle库是可以保存字典,列表,变量数据的

a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

#使用pickle将字典进行保存
file=open('pickle_example.pickle','wb')         #这个文件中的内容用text打开是人眼看不懂的
pickle.dump(a_dict,file)
file.close()

#使用pickle将文件中事先存好的数据读取出来
file=open('pickle_example.pickle','rb')
a_dict1=pickle.load(file)
file.close()
print(a_dict1)              #{'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}


with open('pickle_example.pickle','rb') as file:
    a_dict1=pickle.load(file)
    print(a_dict1)          #{'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}