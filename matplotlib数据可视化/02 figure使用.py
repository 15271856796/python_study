import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)
y1=2*x+1
y2=x**2

#声明一个窗口后,所有的数据都在这个窗口上展示,除非再声明了另一个窗口
plt.figure()
plt.plot(x,y1)

#这里又声明了一个窗口,所有下面的数据又变成在这个窗口上展示
plt.figure(num=3,figsize=(8,5))             #默认这个figure名称是figure2,这里指定num=3的话,是改名叫figure3
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')

plt.show()