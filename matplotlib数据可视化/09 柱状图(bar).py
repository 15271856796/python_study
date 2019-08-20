import matplotlib.pyplot as plt
import numpy as np

n=12
x=np.arange(12)
y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(x,+y1)
plt.bar(x,-y2)

# for x,y in list(zip(x,y1)):
#     plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')

# for x,y in list(zip(x,y2)):
#     plt.text(x+0.4,-y-0.05,'-%.2f'%y,ha='center',va='top')

plt.xlim(5,n)
plt.ylim(-1.25,1.25)
plt.yticks(())
plt.xticks(())

plt.show()