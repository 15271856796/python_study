import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,3,50)
y1=2*x+1
y2=x**2


plt.figure(num=3,figsize=(8,5))             #默认这个figure名称是figure2,这里指定num=3的话,是改名叫figure3
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')

#自定义x轴y轴的标签,用以看每个坐标轴的含义
plt.xlabel('I am x')
plt.ylabel('I am y')

#自定义设置x轴y轴的数据的取值范围 x limit缩写为xlim
plt.xlim((-1,2))
plt.ylim((-2,3))

#自定义设置x轴y轴坐标刻度设置
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)

#plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','normal','good','really good'])          #轴也可以用汉字刻度对应
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])

plt.show()

