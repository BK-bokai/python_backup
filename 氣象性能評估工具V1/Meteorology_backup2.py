#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import re
import xlsxwriter
import datetime
from lib.data_change_Time import data_change_Time
from lib.txt_To_xlsx import txt_To_xlsx


# def txt_To_xlsx(filename):
#     newfilename = filename.split('.')[0]+".xlsx"
#     print(filename+'\n'+'to'+'\n'+newfilename)
#     # 创建工作簿
#     workbook = xlsxwriter.Workbook(newfilename)
#     # 创建工作表
#     worksheet = workbook.add_worksheet('工作表1')
#     index = ['times', '馬祖', '彭佳嶼', '鞍部', '淡水站', '竹子湖', '基隆', '台北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '金門', '梧棲',
#              '台中', '花蓮', '日月潭', '澎湖', '阿里山', '嘉義', '玉山', '東吉島', '七股', '成功', '永康', '台南', '台東', '高雄', '大武', '蘭嶼', '恆春']
#     for i in range(len(index)):
#         worksheet.write(0, i, index[i])
#     x = 1
#     with open(filename, 'r') as data:
#         while True:
#             # 按行循环，读取文本文件
#             line = data.readline()
#             if not line:
#                 break  # 如果没有内容，则退出循环
#             for i in range(len(re.split(r'\s+', line.strip(' ')))):
#                 item = re.split(r'\s+', line.strip(' '))[i]
#                 worksheet.write(x, i, item)  # x单元格经度，i 单元格纬度
#             x += 1  # excel另起一行
#         workbook.close()
#     return newfilename


simdata = txt_To_xlsx(filename='371_MODIS_UCM_T2_201606.txt')
obsdata = '201606obs.xlsx'


# def data_change_Time(obsdata, simdata):
#     obs = pd.read_excel(obsdata)
#     sim = pd.read_excel(simdata)

#     new_time_obsdate = 'new_time_'+obsdata
#     new_time_simdate = 'new_time_'+simdata

#     if not(os.path.isfile(new_time_obsdate)):
#         for i in range(0, len(obs['GMT00    GMT08'])):
#             # 將檔名的年份與檔案內時間結合
#             obs['GMT00    GMT08'][i] = obsdata[0:4] + \
#                 obs['GMT00    GMT08'][i][0:8]
#             # 透過datetime轉換成時間格式再加8小時
#             obstime = (datetime.datetime.strptime(
#                 obs['GMT00    GMT08'][i], '%Y%m-%d-%H')+datetime.timedelta(hours=8))
#             # 最後再覆蓋回檔案讓時間可以比較
#             obs['GMT00    GMT08'][i] = obstime

#         obs.to_excel(new_time_obsdate, index=False)

#     if not(os.path.isfile(new_time_simdate)):
#         for i in range(0, len(sim['times'])):
#             # 取出檔案內的時間，透過datetime轉換成時間格式再加8小時
#             simtime = (datetime.datetime.strptime(
#                 sim['times'][i][11:24], '%Y-%m-%d_%H')+datetime.timedelta(hours=8))
#             # 最後再覆蓋回檔案讓時間可以比較
#             sim['times'][i] = simtime

#         sim.to_excel(new_time_simdate, index=False)

#     return {'obsdata': new_time_obsdate, 'simdata': new_time_simdate}


new_time_data = data_change_Time(obsdata=obsdata, simdata=simdata)

obs = pd.read_excel(new_time_data['obsdata'])
sim = pd.read_excel(new_time_data['simdata'])


stons = []
for item in sim:
    stons.append(item)
stons.pop(0)

MBE = {ston: 0 for ston in stons}

for ston in stons:
    sim_hr_num=0
    for i in range(0,len(obs['GMT00    GMT08'])):
        for j in range(0,len(sim['times'])):
            if (obs['GMT00    GMT08'][i]==sim['times'][j]) and (float(obs[ston][i]) < 999.) and (float(sim[ston][j]) < 999.):
                sim_hr_num += 1 #總共模擬的小時
                tmp=sim[ston][j]-obs[ston][i] #if float(obs[ston][i])<999. else 999.
                MBE[ston] += tmp

    # print(ston+"總共模擬"+str(sim_hr_num)+"小時")
    if (sim_hr_num != 0):
        MBE[ston] = MBE[ston]/(sim_hr_num)
    else:
        MBE[ston] = None
    print(ston+''+'MBE='+str(MBE[ston]))


print('finish')
