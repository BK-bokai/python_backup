#!/usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv

# obs = pd.read_csv('obs.csv')
obs = pd.read_excel("201610obs.xlsx")
sim = pd.read_excel("201610sim.xlsx")

days=31
hours=days*24

x2 = sim["current_date"]
# x2 = sim["GMT00    GMT08"]


stons=[]
stons_obs_avg={}
stons_sim_avg={}

i=0


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
for key, value in obs.items() :
    i=i+1
    if(i==1):
        continue
    stons.append(key)

for ston in stons:
    ston_obs_avg = np.zeros(24)
    for i in range(0, hours, 24):
        ston_obs_avg[0:24] = obs[ston][i:i+24]+ston_obs_avg[0:24]
    stons_obs_avg[ston] =ston_obs_avg[0:24]/days
    
    ston_sim_avg = np.zeros(24)
    for i in range(0, hours, 24):
        ston_sim_avg[0:24] = sim[ston][i:i+24]+ston_sim_avg[0:24]
    stons_sim_avg[ston] =ston_sim_avg[0:24]/days

    plt.close('all')
    plt.rcParams['figure.dpi'] = 500
    plt.figure(figsize=(10, 4.6))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(x2[0:24], stons_obs_avg[ston][0:24],
         color='black', lw=3, label= 'obs')
    plt.plot(x2[0:24], stons_sim_avg[ston][0:24],
         color='red', lw=3, label= 'sim_ucm')

    plt.xlabel("UTC-Time", fontsize=20)
    plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
    plt.title( ston+"_2016-"+(x2[0][0:2]), fontsize=20)
    plt.legend(loc='best', fontsize=17)
    plt.xticks(rotation=70)
    plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\WRF371.SHIFT.NEWLANDUSE.MODIS.UCM3\\10月\\10月img\\2016-" +
            x2[0][0:2]+ston+".png", dpi=500, format="png")



with open("201610obs_avg.csv", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['UTC','台北', '板橋', '新竹', '宜蘭', '花蓮', '梧棲', '台中', '嘉義', '永康', '台南', '台東', '高雄', '恆春'])
    for i in range(0,24):
        writer.writerow([x2[i],stons_obs_avg['台北'][i],stons_obs_avg['板橋'][i],stons_obs_avg['新竹'][i],
                         stons_obs_avg['宜蘭'][i],stons_obs_avg['花蓮'][i],stons_obs_avg['梧棲'][i],stons_obs_avg['台中'][i],
                         stons_obs_avg['嘉義'][i],stons_obs_avg['永康'][i],stons_obs_avg['台南'][i],
                         stons_obs_avg['台東'][i],stons_obs_avg['高雄'][i],stons_obs_avg['恆春'][i]])

with open("201606sim_avg.csv", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['UTC','台北', '板橋', '新竹', '宜蘭', '花蓮', '梧棲', '台中', '嘉義', '永康', '台南', '台東', '高雄', '恆春'])
    for i in range(0,24):
        writer.writerow([x2[i],stons_sim_avg['台北'][i],stons_sim_avg['板橋'][i],stons_sim_avg['新竹'][i],
                         stons_sim_avg['宜蘭'][i],stons_sim_avg['花蓮'][i],stons_sim_avg['梧棲'][i],stons_sim_avg['台中'][i],
                         stons_sim_avg['嘉義'][i],stons_sim_avg['永康'][i],stons_sim_avg['台南'][i],
                         stons_sim_avg['台東'][i],stons_sim_avg['高雄'][i],stons_sim_avg['恆春'][i]])

    





