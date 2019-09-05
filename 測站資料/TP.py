import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

taipei = pd.read_csv('466920-2019-05-26.csv')

time = taipei["ObsTime"]
temp = taipei["Temperature"]
RH   = taipei["RH"]

# print(x1)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(time, temp, linestyle='-', color='pink', label='Temperature')
ax1.set_ylabel('Temperature')#給左邊的Y軸說明
ax1.set_title("Double Y axis")
plt.legend(loc='best')

ax2 = ax1.twinx()  # this is the important function
ax2.plot(time, RH, linestyle='-', color='green', label='RH')#畫在右邊的值
# ax2.set_xlim([0, np.e])
ax2.set_ylabel('RH')#給右邊的Y軸說明
ax2.set_xlabel('Same X for both exp(-x) and ln(x)')
plt.legend(loc='best')
plt.show()





# plt.xticks(range(1,24,1))#給X軸自訂刻度
# plt.yticks(np.arange(0,24,2))#給y軸自訂刻度

# plt.show()