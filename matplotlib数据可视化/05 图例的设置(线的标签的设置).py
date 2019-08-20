import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,3,50)
y1=2*x+1
y2=x**2
plt.figure(num=3,figsize=(8,5))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.xlim((-1,2))
plt.ylim((-2,3))
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#label来设置图例名称,光加一个label标签不行,还必须用legend才能显示标签
plt.plot(x,y2,label='y2=x**2')
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--',label='y1=2*x+1')
plt.legend()

#上面是默认的显示,下面是自定义的显示,
# l1,=plt.plot(x,y2,label='y2=x**2')
# l2,=plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--',label='y1=2*x+1')
#plt.legend(handles=[l1,l2,],labels=['aaa','bbbb'],loc='best')

plt.show()

