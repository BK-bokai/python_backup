import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

obs = pd.read_csv('obs.csv')


_obs = obs["Chiayi"]
YUSHAN_obs = obs["YUSHAN"]
YONGKANG_obs = obs["YONGKANG"]
Tainan_obs = obs["Tainan"]
KAOHSIUNG_obs = obs["KAOHSIUNG"]
DAWU_obs = obs["DAWU"]
HENGCHUN_obs = obs["HENGCHUN"]
x1=obs["GMT00    GMT08"]

simu = pd.read_csv('simu.csv')

Chiayi_simu = simu["Chiayi"]
YUSHAN_simu = simu["YUSHAN"]
YONGKANG_simu = simu["YONGKANG"]
Tainan_simu = simu["Tainan"]
KAOHSIUNG_simu = simu["KAOHSIUNG"]
DAWU_simu = simu["DAWU"]
HENGCHUN_simu = simu["HENGCHUN"]
x2=simu["current_date"]


# plt.subplot(211)
plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[0:24],HENGCHUN_obs[0:24],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[0:24],HENGCHUN_simu[0:24],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-22")
plt.legend(loc='best')

plt.savefig("2019-01-22.png",dpi=300,format="png")


# plt.subplot(212)
plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[24:48],HENGCHUN_obs[24:48],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[24:48],HENGCHUN_simu[24:48],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-23")
plt.legend(loc='best')

plt.savefig("2019-01-23.png",dpi=300,format="png")


plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[48:72],HENGCHUN_obs[48:72],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[48:72],HENGCHUN_simu[48:72],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-24")
plt.legend(loc='best')

plt.savefig("2019-01-24.png",dpi=300,format="png")

plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[72:96],HENGCHUN_obs[72:96],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[72:96],HENGCHUN_simu[72:96],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-25")
plt.legend(loc='best')

plt.savefig("2019-01-25.png",dpi=300,format="png")

plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[96:120],HENGCHUN_obs[96:120],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[96:120],HENGCHUN_simu[96:120],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-26")
plt.legend(loc='best')

plt.savefig("2019-01-26.png",dpi=300,format="png")

plt.close('all')
plt.figure(figsize=(30, 5))
plt.plot(x2[120:144],HENGCHUN_obs[120:144],color='black',lw=3,label='HENGCHUN_obs')
plt.plot(x2[120:144],HENGCHUN_simu[120:144],color='green',lw=3,label='HENGCHUN_simu')
plt.xlabel("UTC-Time")
plt.ylabel('Temperature')#給左邊的Y軸說明
plt.title("2019-01-27")
plt.legend(loc='best')

plt.savefig("2019-01-27.png",dpi=300,format="png")