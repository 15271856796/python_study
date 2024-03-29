import matplotlib.pyplot as plt
import numpy as np

n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(y,x)       #颜色

#alpha是透明度
plt.scatter(x,y,s=75,c=t,alpha=0.5)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
#下面的设置是为了不要轴刻度
plt.xticks(())
plt.yticks(())

plt.show()