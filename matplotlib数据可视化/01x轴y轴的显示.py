import matplotlib.pyplot as plt
import numpy as np

#所有数据显示在一张figure上,所以就不用声明figure
x=np.linspace(-1,1,50)
y=2*x+1
#plot的参数,在前面的是x轴数据,在后面的是y轴数据
plt.plot(x,y)
plt.show()