import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

obs = pd.read_csv('obs.csv')

Chiayi_obs = obs["Chiayi"]

# x1=obs["GMT00    GMT08"]

simu1 = pd.read_csv('simu.csv')

Chiayi_simu1 = simu1["Chiayi"]

x2=simu1["current_date"]

simu2 = pd.read_csv('simu2.csv')

Chiayi_simu2 = simu2["Chiayi"]



for i in range(0,144,24):
    datetitle="2019-"+(x2[i])
    print(datetitle,i,i+24)
    # fig = plt.gcf()
    # plt.close('all')
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex = True, sharey = True, figsize = (30, 7))

    ax1.plot(x2[i:i+24],Chiayi_obs[i:i+24],color='black',lw=3,label='Chiayi_obs')
    ax1.plot(x2[i:i+24],Chiayi_simu1[i:i+24],color='green',lw=3,label='Chiayi_simu')
    ax1.set_xlabel("UTC-Time")
    ax1.set_ylabel('Temperature')#給左邊的Y軸說明
    ax1.set_title("2019-"+(x2[i]))
    ax1.legend(loc='best')
    ax1.set_xticklabels(x2, rotation=70)
    # ax1.tick_params(labelrotation=70)
    # plt.xticks(rotation=70)

    # plt.figure(figsize=(30, 7)).add_subplot(122)
    # # # plt.close('all')
    ax2.plot(x2[i:i+24],Chiayi_obs[i:i+24],color='black',lw=3,label='Chiayi_obs')
    ax2.plot(x2[i:i+24],Chiayi_simu2[i:i+24],color='green',lw=3,label='Chiayi_simu')
    ax2.set_xlabel("UTC-Time")
    ax2.set_ylabel('Temperature')#給左邊的Y軸說明
    ax2.set_title("2019-"+(x2[i]))
    ax2.legend(loc='best')
    ax2.set_xticklabels(x2, rotation=70)
    # plt.xticks(rotation=70)

    # plt.show()
    plt.savefig("2019-"+(x2[i])+"_Chiayi.png",dpi=500,format="png")
    plt.cla
    plt.close()

# fig, (ax1, ax2) = plt.subplots(1, 2, sharex = True, sharey = True, figsize = (30, 7))

# ax1.plot(x2[0:24],Chiayi_obs[0:24],color='black',lw=3,label='Chiayi_obs')
# ax1.plot(x2[0:24],Chiayi_simu1[0:24],color='green',lw=3,label='Chiayi_simu1')
# ax1.set_xlabel("UTC-Time")
# ax1.set_ylabel('Temperature')#給左邊的Y軸說明
# ax1.set_title("2019-01-22")
# ax1.legend(loc='best')
# ax1.set_xticklabels(x2, rotation=70)
# # ax1.tick_params(labelrotation=70)
# # plt.xticks(rotation=70)

# # plt.figure(figsize=(30, 7)).add_subplot(122)
# # # # plt.close('all')
# ax2.plot(x2[0:24],Chiayi_obs[0:24],color='black',lw=3,label='Chiayi_obs')
# ax2.plot(x2[0:24],Chiayi_simu2[0:24],color='green',lw=3,label='Chiayi_simu')
# ax2.set_xlabel("UTC-Time")
# ax2.set_ylabel('Temperature')#給左邊的Y軸說明
# ax2.set_title("2019-01-22")
# ax2.legend(loc='best')
# ax2.set_xticklabels(x2, rotation=70)
# # plt.xticks(rotation=70)

# plt.show()

# plt.savefig("2019-01-22_Chiayi.png",dpi=900,format="png")


# # plt.subplot(212)
# plt.close('all')
# plt.figure(figsize=(30, 5))
# plt.plot(x2[24:48],Chiayi_obs[24:48],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[24:48],Chiayi_simu1[24:48],color='green',lw=3,label='Chiayi_simu1')
# plt.xlabel("UTC-Time")
# plt.ylabel('Temperature')#給左邊的Y軸說明
# plt.title("2019-01-23")
# plt.legend(loc='best')

# plt.savefig("2019-01-23.png",dpi=300,format="png")


# plt.close('all')
# plt.figure(figsize=(30, 5))
# plt.plot(x2[48:72],Chiayi_obs[48:72],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[48:72],Chiayi_simu1[48:72],color='green',lw=3,label='Chiayi_simu1')
# plt.xlabel("UTC-Time")
# plt.ylabel('Temperature')#給左邊的Y軸說明
# plt.title("2019-01-24")
# plt.legend(loc='best')

# plt.savefig("2019-01-24.png",dpi=300,format="png")

# plt.close('all')
# plt.figure(figsize=(30, 5))
# plt.plot(x2[72:96],Chiayi_obs[72:96],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[72:96],Chiayi_simu1[72:96],color='green',lw=3,label='Chiayi_simu1')
# plt.xlabel("UTC-Time")
# plt.ylabel('Temperature')#給左邊的Y軸說明
# plt.title("2019-01-25")
# plt.legend(loc='best')

# plt.savefig("2019-01-25.png",dpi=300,format="png")

# plt.close('all')
# plt.figure(figsize=(30, 5))
# plt.plot(x2[96:120],Chiayi_obs[96:120],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[96:120],Chiayi_simu1[96:120],color='green',lw=3,label='Chiayi_simu1')
# plt.xlabel("UTC-Time")
# plt.ylabel('Temperature')#給左邊的Y軸說明
# plt.title("2019-01-26")
# plt.legend(loc='best')

# plt.savefig("2019-01-26.png",dpi=300,format="png")

# plt.close('all')
# plt.figure(figsize=(30, 5))
# plt.plot(x2[120:144],Chiayi_obs[120:144],color='black',lw=3,label='Chiayi_obs')
# plt.plot(x2[120:144],Chiayi_simu1[120:144],color='green',lw=3,label='Chiayi_simu1')
# plt.xlabel("UTC-Time")
# plt.ylabel('Temperature')#給左邊的Y軸說明
# plt.title("2019-01-27")
# plt.legend(loc='best')

# plt.savefig("2019-01-27.png",dpi=300,format="png")