import numpy as np
import pandas

#使用np.array来定义数组
a=np.array([[1,2,3],[2,3,4]])

print(a)            #输出矩阵[[1 2 3],[2 3 4]]

#输出矩阵的维数,到底是一维的.二维的还是三维的
print('number of dim:',a.ndim)                  #number of dim: 2

#输出矩阵的形状,到底是几行几列的
print('shape:',a.shape)                         #shape: (2, 3)

#输出矩阵的大小
print('size:',a.size)                           #size: 6


#用list来创建矩阵
a=np.array([2,23,4],dtype=np.int)
print(a)                        #[ 2 23  4]
print(a.shape)                  #(3,)
print(a.ndim)                   #1

#用numpy直接生成矩阵(元素都是0)
ａ=np.zeros((3,4))                              #(3,4)是矩阵的形状 [[0. 0. 0. 0.] [0. 0. 0. 0.] [0. 0. 0. 0.]]
print(a)

#生成序列
a=np.arange(10,20,2)
print(a)                            #[10 12 14 16 18]    从10开始,直到20,步长为2
print(type(a))                      #<class 'numpy.ndarray'>



#生成一个0到11的序列,并将序列转化成3行4列的数组
a=np.arange(12)
print(a)                            #[ 0  1  2  3  4  5  6  7  8  9 10 11]
a=np.arange(12).reshape((3,4))      #[[ 0  1  2  3]
                                    #[ 4  5  6  7]
                                    #[ 8  9 10 11]]


#numpy生成序列,和上面生成方法不一样的地方是,第三个参数不代表步长,而代表的是到底生成多少个

a=np.linspace(1,10,6)                   #[ 1.   2.8  4.6  6.4  8.2 10. ]
print(a)

a.reshape(2,3)
print(a)


#元素随机生成
a=np.random.random((2,4))           #[[0.97982099 0.67078156 0.29605819 0.8416442 ]
                                    #[0.10695245 0.47205753 0.29246948 0.23817815]]
print(a)