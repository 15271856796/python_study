import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,3,50)
y1=2*x+1
y2=x**2
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.xlim((-1,2))
plt.ylim((-2,3))
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])


#设置原点的位置,默认显示的是最小的(x,y)的坐标,没有四个坐标域,默认只有一个坐标域
ax=plt.gca()
#默认的时候四个框都是实线,现在只想显示两个线来表示x,y轴
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#轴的设置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#原点坐标的设置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()

