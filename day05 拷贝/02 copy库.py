import copy

a=[1,2,3,4]
b=copy.copy(a)
b.append(7)
print(a,b)                  #[1, 2, 3, 4] [1, 2, 3, 4, 7]

a={'1':2,'2':3}
b=copy.copy(a)
b['3']=4
print(a,b)                  #{'1': 2, '2': 3} {'1': 2, '2': 3, '3': 4}

#copy.copy()只能实现最外层的copy值
a=[1,2,3,[7,8]]
b=copy.copy(a)
print("a=%s,b=%s"%(a,b))            #a=[1, 2, 3, [7, 8]],b=[1, 2, 3, [7, 8]]
a[1]=22
a[3][1]=88
print("a=%s,b=%s"%(a,b))            #a=[1, 22, 3, [7, 88]],b=[1, 2, 3, [7, 88]]


#为了实现完全的copy   copy.deepcopy()

a=[1,2,3,[7,8]]
b=copy.deepcopy(a)
print("a=%s,b=%s"%(a,b))                    #a=[1, 2, 3, [7, 8]],b=[1, 2, 3, [7, 8]]
a[3][1]=88
print("a=%s,b=%s"%(a,b))                    #a=[1, 2, 3, [7, 88]],b=[1, 2, 3, [7, 8]]
