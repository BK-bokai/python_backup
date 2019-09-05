import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv

# obs = pd.read_csv('obs.csv')
obs = pd.read_excel("obs.xlsx")
ucm = pd.read_excel("cla3080100.xlsx")
contr = pd.read_excel("contr.xlsx")

x2 = contr["current_date"]

stons=[]
stons_obs_avg={}
stons_ucm_avg={}
stons_contr_avg={}
i=0


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
for key, value in obs.items() :
    i=i+1
    if(i==1):
        continue
    stons.append(key)
# print(stons)

for ston in stons:
    ston_obs_avg = np.zeros(24)
    for i in range(0, 744, 24):
        ston_obs_avg[0:24] = obs[ston][i:i+24]+ston_obs_avg[0:24]
    stons_obs_avg[ston] =ston_obs_avg[0:24]/31
    
    ston_ucm_avg = np.zeros(24)
    for i in range(0, 744, 24):
        ston_ucm_avg[0:24] = ucm[ston][i:i+24]+ston_ucm_avg[0:24]
    stons_ucm_avg[ston] =ston_ucm_avg[0:24]/31

    ston_contr_avg = np.zeros(24)
    for i in range(0, 744, 24):
        ston_contr_avg[0:24] = contr[ston][i:i+24]+ston_contr_avg[0:24]
    stons_contr_avg[ston] =ston_contr_avg[0:24]/31

    plt.close('all')
    plt.rcParams['figure.dpi'] = 500
    plt.figure(figsize=(10, 4.8))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(x2[0:24], stons_obs_avg[ston][0:24],
         color='black', lw=3, label= 'obs')
    plt.plot(x2[0:24], stons_ucm_avg[ston][0:24],
         color='red', lw=3, label= 'ucm')
    plt.plot(x2[0:24], stons_contr_avg[ston][0:24],
         color='blue', lw=3, label= 'contral')
    plt.xlabel("UTC-Time", fontsize=20)
    plt.ylabel('Temperature', fontsize=20)  # 給左邊的Y軸說明
    plt.title( ston+"_2016-"+(x2[0][0:2]), fontsize=20)
    plt.legend(loc='best', fontsize=17)
    plt.xticks(rotation=70)
    plt.savefig("D:\\bokai\\python\\python-code\\氣象性能評估\\UCMtest\\201612\\img\\2016-" +
            (x2[0][0:2])+ston+".png", dpi=500, format="png")


with open("201612obs_avg.csv", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['UTC','台北', '板橋', '新竹', '宜蘭', '梧棲', '台中', '嘉義', '永康', '台南', '台東', '高雄', '恆春'])
    for i in range(0,24):
        writer.writerow([x2[i],stons_obs_avg['台北'][i],stons_obs_avg['板橋'][i],stons_obs_avg['新竹'][i],
                         stons_obs_avg['宜蘭'][i],stons_obs_avg['梧棲'][i],stons_obs_avg['台中'][i],
                         stons_obs_avg['嘉義'][i],stons_obs_avg['永康'][i],stons_obs_avg['台南'][i],
                         stons_obs_avg['台東'][i],stons_obs_avg['高雄'][i],stons_obs_avg['恆春'][i]])


    





