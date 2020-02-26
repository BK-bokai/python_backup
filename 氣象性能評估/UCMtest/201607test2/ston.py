import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

# obs = pd.read_csv('obs.csv')
obs_avg = np.zeros((24, 6))


obs = pd.read_excel("obs.xlsx")

Taichung_obs = obs["台中"]
Chiayi_obs = obs["嘉義"]
Yongkang_obs = obs["永康"]
Tainan_obs = obs["台南"]
Kaohsiung_obs = obs["高雄"]
Taipei_obs = obs["台北"]
Banqiao_obs = obs["板橋"]
Hsinchu_obs = obs["新竹"]
Yilan_obs = obs["宜蘭"]
Hengchun_obs= obs["恆春"]

x1 = obs["GMT00    GMT08"]


Taichung_obs_avg = np.zeros(24)
Chiayi_obs_avg = np.zeros(24)
Yongkang_obs_avg = np.zeros(24)
Tainan_obs_avg = np.zeros(24)
Kaohsiung_obs_avg = np.zeros(24)
Taipei_obs_avg = np.zeros(24)
Banqiao_obs_avg = np.zeros(24)
Hsinchu_obs_avg = np.zeros(24)
Yilan_obs_avg = np.zeros(24)
Hengchun_obs_avg = np.zeros(24)

for i in range(0, 744, 24):
    Taichung_obs_avg[0:24] = Taichung_obs[i:i+24]+Taichung_obs_avg[0:24]

for i in range(0, 744, 24):
    Chiayi_obs_avg[0:24] = Chiayi_obs[i:i+24]+Chiayi_obs_avg[0:24]

for i in range(0, 744, 24):
    Yongkang_obs_avg[0:24] = Yongkang_obs[i:i+24]+Yongkang_obs_avg[0:24]

for i in range(0, 744, 24):
    Tainan_obs_avg[0:24] = Tainan_obs[i:i+24]+Tainan_obs_avg[0:24]

for i in range(0, 744, 24):
    Kaohsiung_obs_avg[0:24] = Kaohsiung_obs[i:i+24]+Kaohsiung_obs_avg[0:24]

for i in range(0, 744, 24):
    Taipei_obs_avg[0:24] = Taipei_obs[i:i+24]+Taipei_obs_avg[0:24]

for i in range(0, 744, 24):
    Banqiao_obs_avg[0:24] = Banqiao_obs[i:i+24]+Banqiao_obs_avg[0:24]

for i in range(0, 744, 24):
    Hsinchu_obs_avg[0:24] = Hsinchu_obs[i:i+24]+Hsinchu_obs_avg[0:24]

for i in range(0, 744, 24):
    Yilan_obs_avg[0:24] = Yilan_obs[i:i+24]+Yilan_obs_avg[0:24]

for i in range(0, 744, 24):
    Hengchun_obs_avg[0:24] = Hengchun_obs[i:i+24]+Hengchun_obs_avg[0:24]

Taichung_obs_avg[0:24] = Taichung_obs_avg[0:24]/24
Chiayi_obs_avg[0:24] = Chiayi_obs_avg[0:24]/24
Yongkang_obs_avg[0:24] = Yongkang_obs_avg[0:24]/24
Tainan_obs_avg[0:24] = Tainan_obs_avg[0:24]/24
Kaohsiung_obs_avg[0:24] = Kaohsiung_obs_avg[0:24]/24
Taipei_obs_avg[0:24] = Taipei_obs_avg[0:24]/24
Banqiao_obs_avg[0:24] = Banqiao_obs_avg[0:24]/24
Hsinchu_obs_avg[0:24] = Hsinchu_obs_avg[0:24]/24
Yilan_obs_avg[0:24] = Yilan_obs_avg[0:24]/24
Hengchun_obs_avg[0:24] = Hengchun_obs_avg[0:24]/24

# simu = pd.read_csv('simu.csv')
normal = pd.read_excel("normal.xlsx")

Taichung_nor = normal["台中"]
Chiayi_nor = normal["嘉義"]
Yongkang_nor = normal["永康"]
Tainan_nor = normal["台南"]
Kaohsiung_nor = normal["高雄"]
Taipei_nor = normal["台北"]
Banqiao_nor = normal["板橋"]
Hsinchu_nor = normal["新竹"]
Yilan_nor = normal["宜蘭"]
Hengchun_nor= normal["恆春"]


x2 = normal["current_date"]


Taichung_nor_avg = np.zeros(24)
Chiayi_nor_avg = np.zeros(24)
Yongkang_nor_avg = np.zeros(24)
Tainan_nor_avg = np.zeros(24)
Kaohsiung_nor_avg = np.zeros(24)
Taipei_nor_avg = np.zeros(24)
Banqiao_nor_avg = np.zeros(24)
Hsinchu_nor_avg = np.zeros(24)
Yilan_nor_avg = np.zeros(24)
Hengchun_nor_avg = np.zeros(24)

for i in range(0, 744, 24):
    Taichung_nor_avg[0:24] = Taichung_nor[i:i+24]+Taichung_nor_avg[0:24]

for i in range(0, 744, 24):
    Chiayi_nor_avg[0:24] = Chiayi_nor[i:i+24]+Chiayi_nor_avg[0:24]

for i in range(0, 744, 24):
    Yongkang_nor_avg[0:24] = Yongkang_nor[i:i+24]+Yongkang_nor_avg[0:24]

for i in range(0, 744, 24):
    Tainan_nor_avg[0:24] = Tainan_nor[i:i+24]+Tainan_nor_avg[0:24]

for i in range(0, 744, 24):
    Kaohsiung_nor_avg[0:24] = Kaohsiung_nor[i:i+24]+Kaohsiung_nor_avg[0:24]

for i in range(0, 744, 24):
    Taipei_nor_avg[0:24] = Taipei_nor[i:i+24]+Taipei_nor_avg[0:24]

for i in range(0, 744, 24):
    Banqiao_nor_avg[0:24] = Banqiao_nor[i:i+24]+Banqiao_nor_avg[0:24]

for i in range(0, 744, 24):
    Hsinchu_nor_avg[0:24] = Hsinchu_nor[i:i+24]+Hsinchu_nor_avg[0:24]

for i in range(0, 744, 24):
    Yilan_nor_avg[0:24] = Yilan_nor[i:i+24]+Yilan_nor_avg[0:24]

for i in range(0, 744, 24):
    Hengchun_nor_avg[0:24] = Hengchun_nor[i:i+24]+Hengchun_nor_avg[0:24]

Taichung_nor_avg[0:24] = Taichung_nor_avg[0:24]/24
Chiayi_nor_avg[0:24] = Chiayi_nor_avg[0:24]/24
Yongkang_nor_avg[0:24] = Yongkang_nor_avg[0:24]/24
Tainan_nor_avg[0:24] = Tainan_nor_avg[0:24]/24
Kaohsiung_nor_avg[0:24] = Kaohsiung_nor_avg[0:24]/24
Taipei_nor_avg[0:24] = Taipei_nor_avg[0:24]/24
Banqiao_nor_avg[0:24] = Banqiao_nor_avg[0:24]/24
Hsinchu_nor_avg[0:24] = Hsinchu_nor_avg[0:24]/24
Yilan_nor_avg[0:24] = Yilan_nor_avg[0:24]/24
Hengchun_nor_avg[0:24] = Hengchun_nor_avg[0:24]/24


# simu = pd.read_csv('simu.csv')
cla3080100 = pd.read_excel("cla3080100.xlsx")

Taichung_cla = cla3080100["台中"]
Chiayi_cla = cla3080100["嘉義"]
Yongkang_cla = cla3080100["永康"]
Tainan_cla = cla3080100["台南"]
Kaohsiung_cla = cla3080100["高雄"]
Taipei_cla = cla3080100["台北"]
Banqiao_cla = cla3080100["板橋"]
Hsinchu_cla = cla3080100["新竹"]
Yilan_cla = cla3080100["宜蘭"]
Hengchun_cla = cla3080100["恆春"]



Taichung_cla_avg = np.zeros(24)
Chiayi_cla_avg = np.zeros(24)
Yongkang_cla_avg = np.zeros(24)
Tainan_cla_avg = np.zeros(24)
Kaohsiung_cla_avg = np.zeros(24)
Taipei_cla_avg = np.zeros(24)
Banqiao_cla_avg = np.zeros(24)
Hsinchu_cla_avg = np.zeros(24)
Yilan_cla_avg = np.zeros(24)
Hengchun_cla_avg = np.zeros(24)

for i in range(0, 744, 24):
    Taichung_cla_avg[0:24] = Taichung_cla[i:i+24]+Taichung_cla_avg[0:24]

for i in range(0, 744, 24):
    Chiayi_cla_avg[0:24] = Chiayi_cla[i:i+24]+Chiayi_cla_avg[0:24]

for i in range(0, 744, 24):
    Yongkang_cla_avg[0:24] = Yongkang_cla[i:i+24]+Yongkang_cla_avg[0:24]

for i in range(0, 744, 24):
    Tainan_cla_avg[0:24] = Tainan_cla[i:i+24]+Tainan_cla_avg[0:24]

for i in range(0, 744, 24):
    Kaohsiung_cla_avg[0:24] = Kaohsiung_cla[i:i+24]+Kaohsiung_cla_avg[0:24]

for i in range(0, 744, 24):
    Taipei_cla_avg[0:24] = Taipei_cla[i:i+24]+Taipei_cla_avg[0:24]

for i in range(0, 744, 24):
    Banqiao_cla_avg[0:24] = Banqiao_cla[i:i+24]+Banqiao_cla_avg[0:24]

for i in range(0, 744, 24):
    Hsinchu_cla_avg[0:24] = Hsinchu_cla[i:i+24]+Hsinchu_cla_avg[0:24]

for i in range(0, 744, 24):
    Yilan_cla_avg[0:24] = Yilan_cla[i:i+24]+Yilan_cla_avg[0:24]

for i in range(0, 744, 24):
    Hengchun_cla_avg[0:24] = Hengchun_cla[i:i+24]+Hengchun_cla_avg[0:24]

Taichung_cla_avg[0:24] = Taichung_cla_avg[0:24]/24
Chiayi_cla_avg[0:24] = Chiayi_cla_avg[0:24]/24
Yongkang_cla_avg[0:24] = Yongkang_cla_avg[0:24]/24
Tainan_cla_avg[0:24] = Tainan_cla_avg[0:24]/24
Kaohsiung_cla_avg[0:24] = Kaohsiung_cla_avg[0:24]/24
Taipei_cla_avg[0:24] = Taipei_cla_avg[0:24]/24
Banqiao_cla_avg[0:24] = Banqiao_cla_avg[0:24]/24
Hsinchu_cla_avg[0:24] = Hsinchu_cla_avg[0:24]/24
Yilan_cla_avg[0:24] = Yilan_cla_avg[0:24]/24
Hengchun_cla_avg[0:24] = Hengchun_cla_avg[0:24]/24

# simu = pd.read_csv('simu.csv')
contr = pd.read_excel("contr.xlsx")

Taichung_con = contr["台中"]
Chiayi_con = contr["嘉義"]
Yongkang_con = contr["永康"]
Tainan_con = contr["台南"]
Kaohsiung_con = contr["高雄"]
Taipei_con = contr["台北"]
Banqiao_con = contr["板橋"]
Hsinchu_con = contr["新竹"]
Yilan_con = contr["宜蘭"]
Hengchun_con = contr["恆春"]


Taichung_con_avg = np.zeros(24)
Chiayi_con_avg = np.zeros(24)
Yongkang_con_avg = np.zeros(24)
Tainan_con_avg = np.zeros(24)
Kaohsiung_con_avg = np.zeros(24)
Taipei_con_avg = np.zeros(24)
Banqiao_con_avg = np.zeros(24)
Hsinchu_con_avg = np.zeros(24)
Yilan_con_avg = np.zeros(24)
Hengchun_con_avg = np.zeros(24)

for i in range(0, 744, 24):
    Taichung_con_avg[0:24] = Taichung_con[i:i+24]+Taichung_con_avg[0:24]

for i in range(0, 744, 24):
    Chiayi_con_avg[0:24] = Chiayi_con[i:i+24]+Chiayi_con_avg[0:24]

for i in range(0, 744, 24):
    Yongkang_con_avg[0:24] = Yongkang_con[i:i+24]+Yongkang_con_avg[0:24]

for i in range(0, 744, 24):
    Tainan_con_avg[0:24] = Tainan_con[i:i+24]+Tainan_con_avg[0:24]

for i in range(0, 744, 24):
    Kaohsiung_con_avg[0:24] = Kaohsiung_con[i:i+24]+Kaohsiung_con_avg[0:24]

for i in range(0, 744, 24):
    Taipei_con_avg[0:24] = Taipei_con[i:i+24]+Taipei_con_avg[0:24]

for i in range(0, 744, 24):
    Banqiao_con_avg[0:24] = Banqiao_con[i:i+24]+Banqiao_con_avg[0:24]

for i in range(0, 744, 24):
    Hsinchu_con_avg[0:24] = Hsinchu_con[i:i+24]+Hsinchu_con_avg[0:24]

for i in range(0, 744, 24):
    Yilan_con_avg[0:24] = Yilan_con[i:i+24]+Yilan_con_avg[0:24]

for i in range(0, 744, 24):
    Hengchun_con_avg[0:24] = Hengchun_con[i:i+24]+Hengchun_con_avg[0:24]

Taichung_con_avg[0:24] = Taichung_con_avg[0:24]/24
Chiayi_con_avg[0:24] = Chiayi_con_avg[0:24]/24
Yongkang_con_avg[0:24] = Yongkang_con_avg[0:24]/24
Tainan_con_avg[0:24] = Tainan_con_avg[0:24]/24
Kaohsiung_con_avg[0:24] = Kaohsiung_con_avg[0:24]/24
Taipei_con_avg[0:24] = Taipei_con_avg[0:24]/24
Banqiao_con_avg[0:24] = Banqiao_con_avg[0:24]/24
Hsinchu_con_avg[0:24] = Hsinchu_con_avg[0:24]/24
Yilan_con_avg[0:24] = Yilan_con_avg[0:24]/24
Hengchun_con_avg[0:24] = Hengchun_con_avg[0:24]/24

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Chiayi_obs_avg[0:24],
         color='black', lw=3, label='Chiayi_obs')
# plt.plot(x2[0:24], Chiayi_nor_avg[0:24],
#          color='green', lw=3, label='Chiayi_normalization')
plt.plot(x2[0:24], Chiayi_cla_avg[0:24],
         color='red', lw=3, label='Chiayi_percentage')
plt.plot(x2[0:24], Chiayi_con_avg[0:24],
         color='blue', lw=3, label='Chiayi_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Chiayi_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Chiayi.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Taichung_obs_avg[0:24],
         color='black', lw=3, label='Taichung_obs')
# plt.plot(x2[0:24], Taichung_nor_avg[0:24],
#          color='green', lw=3, label='Taichung_normalization')
plt.plot(x2[0:24], Taichung_cla_avg[0:24],
         color='red', lw=3, label='Taichung_percentage')
plt.plot(x2[0:24], Taichung_con_avg[0:24],
         color='blue', lw=3, label='Taichung_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Taichung_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Taichung.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Yongkang_obs_avg[0:24],
         color='black', lw=3, label='Yongkang_obs')
# plt.plot(x2[0:24], Yongkang_nor_avg[0:24],
#          color='green', lw=3, label='Yongkang_normalization')
plt.plot(x2[0:24], Yongkang_cla_avg[0:24],
         color='red', lw=3, label='Yongkang_percentage')
plt.plot(x2[0:24], Yongkang_con_avg[0:24],
         color='blue', lw=3, label='Yongkang_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Yongkang_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Yongkang.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Tainan_obs_avg[0:24],
         color='black', lw=3, label='Tainan_obs')
# plt.plot(x2[0:24], Tainan_nor_avg[0:24],
#          color='green', lw=3, label='Tainan_normalization')
plt.plot(x2[0:24], Tainan_cla_avg[0:24],
         color='red', lw=3, label='Tainan_percentage')
plt.plot(x2[0:24], Tainan_con_avg[0:24],
         color='blue', lw=3, label='Tainan_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Tainan_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Tainan.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Kaohsiung_obs_avg[0:24],
         color='black', lw=3, label='Kaohsiung_obs')
# plt.plot(x2[0:24], Kaohsiung_nor_avg[0:24],
#          color='green', lw=3, label='Kaohsiung_normalization')
plt.plot(x2[0:24], Kaohsiung_cla_avg[0:24],
         color='red', lw=3, label='Kaohsiung_percentage')
plt.plot(x2[0:24], Kaohsiung_con_avg[0:24],
         color='blue', lw=3, label='Kaohsiung_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Kaohsiung_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=12)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Kaohsiung.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Taipei_obs_avg[0:24],
         color='black', lw=3, label='Taipei_obs')
# plt.plot(x2[0:24], Taipei_nor_avg[0:24],
#          color='green', lw=3, label='Taipei_normalization')
plt.plot(x2[0:24], Taipei_cla_avg[0:24],
         color='red', lw=3, label='Taipei_percentage')
plt.plot(x2[0:24], Taipei_con_avg[0:24],
         color='blue', lw=3, label='Taipei_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Taipei_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Taipei.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Banqiao_obs_avg[0:24],
         color='black', lw=3, label='Banqiao_obs')
# plt.plot(x2[0:24], Banqiao_nor_avg[0:24],
#          color='green', lw=3, label='Banqiao_normalization')
plt.plot(x2[0:24], Banqiao_cla_avg[0:24],
         color='red', lw=3, label='Banqiao_percentage')
plt.plot(x2[0:24], Banqiao_con_avg[0:24],
         color='blue', lw=3, label='Banqiao_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Banqiao_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Banqiao.png", dpi=500, format="png")


plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Hsinchu_obs_avg[0:24],
         color='black', lw=3, label='Hsinchu_obs')
# plt.plot(x2[0:24], Hsinchu_nor_avg[0:24],
#          color='green', lw=3, label='Hsinchu_normalization')
plt.plot(x2[0:24], Hsinchu_cla_avg[0:24],
         color='red', lw=3, label='Hsinchu_percentage')
plt.plot(x2[0:24], Hsinchu_con_avg[0:24],
         color='blue', lw=3, label='Hsinchu_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Hsinchu_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Hsinchu.png", dpi=500, format="png")

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Yilan_obs_avg[0:24],
         color='black', lw=3, label='Yilan_obs')
# plt.plot(x2[0:24], Yilan_nor_avg[0:24],
#          color='green', lw=3, label='Yilan_normalization')
plt.plot(x2[0:24], Yilan_cla_avg[0:24],
         color='red', lw=3, label='Yilan_percentage')
plt.plot(x2[0:24], Yilan_con_avg[0:24],
         color='blue', lw=3, label='Yilan_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Yilan_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Yilan.png", dpi=500, format="png")

# with open("filename", 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(["台中(都市比例分類)","台中(標準化分類)","嘉義(都市比例分類)","嘉義(標準化分類)",
#                         "永康(都市比例分類)","永康(標準化分類)","台南(都市比例分類)","台南(標準化分類)",
#                         "高雄(都市比例分類)","高雄(標準化分類)"])
#     for i in range(0,24):
#         writer.writerow([Taichung_cla_avg[i],Taichung_nor_avg[i],Chiayi_cla_avg[i],Chiayi_nor_avg[i],
#                         Yongkang_cla_avg[i],Yongkang_nor_avg[i],Tainan_cla_avg[i],Tainan_nor_avg[i],
#                         Kaohsiung_cla_avg[i],Kaohsiung_nor_avg[i]])

plt.close('all')
plt.rcParams['figure.dpi'] = 500
plt.figure(figsize=(10, 4.8))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(x2[0:24], Hengchun_obs_avg[0:24],
         color='black', lw=3, label='Hengchun_obs')
# plt.plot(x2[0:24], Hengchun_nor_avg[0:24],
#          color='green', lw=3, label='Hengchun_normalization')
plt.plot(x2[0:24], Hengchun_cla_avg[0:24],
         color='red', lw=3, label='Hengchun_percentage')
plt.plot(x2[0:24], Hengchun_con_avg[0:24],
         color='blue', lw=3, label='Hengchun_control')
plt.xlabel("UTC-Time", fontsize=20)
plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
plt.title("Hengchun_2019-"+(x2[0][0:2]), fontsize=20)
plt.legend(loc='best', fontsize=17)
plt.xticks(rotation=70)

plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\normal\\img\\2019-" +
            (x2[0][0:2])+"Hengchun.png", dpi=500, format="png")

with open("obsavg", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["台中(obs)","台中(obs)","嘉義(obs)","嘉義(obs)",
                        "永康(obs)","永康(obs)","台南(obs)","台南(obs)",
                        "高雄(obs)","高雄(obs)"])
    for i in range(0,24):
        writer.writerow([Taichung_obs_avg[i],Taichung_obs_avg[i],Chiayi_obs_avg[i],Chiayi_obs_avg[i],
                        Yongkang_obs_avg[i],Yongkang_obs_avg[i],Tainan_obs_avg[i],Tainan_obs_avg[i],
                        Kaohsiung_obs_avg[i],Kaohsiung_obs_avg[i]])





