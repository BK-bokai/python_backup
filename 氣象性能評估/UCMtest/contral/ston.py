import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

obs = pd.read_csv('obs.csv')
Chiayi_obs = obs["Chiayi"]
x1=obs["GMT00    GMT08"]

simu = pd.read_csv('simu.csv')
Chiayi_simu = simu["Chiayi"]
x2=simu["current_date"]



for i in range(0,144,24):
    datetitle="2019-"+(x2[i][0:5])
    print(datetitle,i,i+24)
    plt.close('all')
    plt.rcParams['figure.dpi'] = 500
    plt.figure(figsize=(10, 4.8))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(x2[i:i+24],Chiayi_obs[i:i+24],color='black',lw=3,label='Chiayi_obs')
    plt.plot(x2[i:i+24],Chiayi_simu[i:i+24],color='green',lw=3,label='Chiayi_simu')
    plt.xlabel("UTC-Time" ,fontsize=20)
    plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
    plt.title("2019-"+(x2[i][0:5]), fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xticks(rotation=70)

    plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\Hsinta\\三月\\嘉義\\2019-"+(x2[i][0:5])+"Chiayi.png",dpi=500,format="png")


# plt.close('all')
# plt.rcParams['figure.dpi'] = 500
# plt.figure(figsize=(13, 13))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.plot(x2[24:48],Chiayi_obs[24:48],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[24:48],Chiayi_simu[24:48],color='green',lw=3,label='Chiayi_simu')
# plt.xlabel("UTC-Time" ,fontsize=20)
# plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
# plt.title("2019-03-17", fontsize=20)
# plt.legend(loc='best', fontsize=20)
# plt.xticks(rotation=70)

# plt.savefig("2019-03-17.png",dpi=500,format="png")


# plt.close('all')
# plt.rcParams['figure.dpi'] = 500
# plt.figure(figsize=(13, 13))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.plot(x2[48:72],Chiayi_obs[48:72],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[48:72],Chiayi_simu[48:72],color='green',lw=3,label='Chiayi_simu')
# plt.xlabel("UTC-Time" ,fontsize=20)
# plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
# plt.title("2019-03-18", fontsize=20)
# plt.legend(loc='best', fontsize=20)
# plt.xticks(rotation=70)

# plt.savefig("2019-03-18.png",dpi=500,format="png")

# plt.close('all')
# plt.rcParams['figure.dpi'] = 500
# plt.figure(figsize=(13, 13))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.plot(x2[72:96],Chiayi_obs[72:96],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[72:96],Chiayi_simu[72:96],color='green',lw=3,label='Chiayi_simu')
# plt.xlabel("UTC-Time" ,fontsize=20)
# plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
# plt.title("2019-03-19", fontsize=20)
# plt.legend(loc='best', fontsize=20)
# plt.xticks(rotation=70)

# plt.savefig("2019-03-19.png",dpi=500,format="png")

# plt.close('all')
# plt.rcParams['figure.dpi'] = 500
# plt.figure(figsize=(13, 13))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.plot(x2[96:120],Chiayi_obs[96:120],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[96:120],Chiayi_simu[96:120],color='green',lw=3,label='Chiayi_simu')
# plt.xlabel("UTC-Time" ,fontsize=20)
# plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
# plt.title("2019-03-20", fontsize=20)
# plt.legend(loc='best', fontsize=20)
# plt.xticks(rotation=70)

# plt.savefig("2019-03-20.png",dpi=500,format="png")

# plt.close('all')
# plt.rcParams['figure.dpi'] = 500
# plt.figure(figsize=(13, 13))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.plot(x2[120:144],Chiayi_obs[120:144],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[120:144],Chiayi_simu[120:144],color='green',lw=3,label='Chiayi_simu')
# plt.xlabel("UTC-Time" ,fontsize=20)
# plt.ylabel('Temperature', fontsize=20)#給左邊的Y軸說明
# plt.title("2019-03-21", fontsize=20)
# plt.legend(loc='best', fontsize=20)
# plt.xticks(rotation=70)

# plt.savefig("2019-03-21.png",dpi=500,format="png")