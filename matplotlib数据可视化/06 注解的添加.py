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
plt.plot(x,y1,label='y2=x*2+1')
plt.legend()



x0=0.25
y0=2*x0+1
#在线上标注一个点出来,用scatter是用来显示点的 会一个点一个点的显示出来,plot是用来显示线的
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)

#添加注解method1
plt.annotate(r'$2x+1=%s$' % y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->'))

#method2
plt.text(-3.7,3,r'$this\ is\ the\ some\ text$',fontdict={'size':16,'color':'red'})

plt.show()

