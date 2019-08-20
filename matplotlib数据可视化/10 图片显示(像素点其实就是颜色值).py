import matplotlib.pyplot as plt
import numpy as np

a=np.array([0.313660827,0.3653484454,0.32345647657,
            0.24124234576,0.78776576893,0.146668089898987,
            0.12432546423234,0.45658779657,0.323243576]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
#coloebar是颜色的像素点取值范围,shrink是指定颜色标尺的长度 百分之90
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()