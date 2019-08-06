
#zip就是为迭代器而产生的东西
a=[1,2,3]
b=[5,6,7]
print(zip(a,b))                 #<zip object at 0x00000000028B1188>
print(list(zip(a,b)))           #[(1, 5), (2, 6), (3, 7)]

for i,j in zip(a,b):
    print(i/2,j*2)
    # 0.5 10
    # 1.0 12
    # 1.5 14

print(list(zip(a,a,b)))         #[(1, 1, 5), (2, 2, 6), (3, 3, 7)]
