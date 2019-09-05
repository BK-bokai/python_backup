import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,360,5)
y = np.sin( x * np.pi / 180.0 )

#設定要畫圖的座標軸
# plt.plot(x,y) 
# plt.plot(x,y,lw=2)#lw調整線條寬細
plt.plot(x,y,"o",lw=2)#可以調style及大小


#設定畫圖範圍
plt.xlim(-30,390)
plt.ylim(-1.5,1.5)

#給X軸、Y軸及title名子
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("The Title") 

plt.show()