import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0,360,5)
y1 = np.sin( x1 * np.pi / 180.0 )

x2 = x1
y2 = np.cos( x2 * np.pi / 180.0 )

x3 = x1
y3 = np.tan(x3 * np.pi / 180.0)

plt.subplot(211)
plt.plot(x1,y1,lw=3)
plt.xlim(-30,390)
plt.ylim(-2,2)
plt.xticks(range(0,360,50))#給X軸自訂刻度
plt.yticks(np.arange(-2,2,1))#給y軸自訂刻度


plt.subplot(212)
plt.plot(x2,y2,'ro',lw=3)
plt.xlim(-30,390)
plt.ylim(-2,2)

plt.show()
# plt.savefig("plot.png",dpi=300,format="png")