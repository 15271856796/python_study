
#map用来调用函数

def fun1(x,y):
    return x+y

#map是调用函数的方法,[1,3]是x的传值,[2,4]是y的传值,计算1+2,3+4分别计算
print(list(map(fun1,[1,3],[2,4])))          #[3, 7]