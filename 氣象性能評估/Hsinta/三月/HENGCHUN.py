import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

obs = pd.read_csv('obs.csv')
HENGCHUN_obs = obs["HENGCHUN"]
x1=obs["GMT00    GMT08"]

simu = pd.read_csv('simu.csv')
HENGCHUN_simu = simu["HENGCHUN"]
x2=simu["current_date"]



for i in range(0,144,24):
    datetitle="2019-"+(x2[i][0:5])
    print(datetitle,i,i+24)
    plt.close('all')
    plt.rcParams['figure.dpi'] = 500
    plt.figure(figsize=(10, 4.8))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(x2[i:i+24],HENGCHUN_obs[i:i+24],color='black',lw=3,label='HENGCHUN_obs')
    plt.plot(x2[i:i+24],HENGCHUN_simu[i:i+24],color='green',lw=3,label='HENGCHUN_simu')
    plt.xlabel("UTC-Time" ,fontsize=20)
    plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
    plt.title("2019-"+(x2[i][0:5]), fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xticks(rotation=70)

    plt.savefig("2019-"+(x2[i][0:5])+"HENGCHUN.png",dpi=500,format="png")