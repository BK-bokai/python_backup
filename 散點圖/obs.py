import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import matplotlib.pyplot as plt


obs = pd.read_excel("g19.xlsx")

# N = len(obs['時間'][168:265])
x = obs['時間'][0:144]  # 包含10个均匀分布的随机值的横坐标数组，大小[0, 1]
y = obs['WD'][0:144]  # 包含10个均匀分布的随机值的纵坐标数组
# plt.scatter(x, y, alpha=0.6)  # 绘制散点图，透明度为0.6（这样颜色浅一点，比较好看）
# plt.show()

plt.close('all')
# plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xticks(rotation=70)
plt.plot(x, y,'o')
plt.xticks(range(len(x)),x,rotation=70)
# xticks(location,lables[,rotation])
plt.show()

# plt.xlabel("UTC-Time", fontsize=20)
# plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
# plt.title(ston+"_2016-"+(x2[0][0:2]), fontsize=20)
# plt.legend(loc='best', fontsize=17)
# plt.xticks(rotation=70)
# plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\201607\\img\\2016-" +
#             (x2[0][0:2])+ston+".png", dpi=500, format="png")
