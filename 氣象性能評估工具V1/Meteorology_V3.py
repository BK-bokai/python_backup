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


simdata = txt_To_xlsx(filename='371_MODIS_UCM_T2_201606.txt')
obsdata = '201606obs.xlsx'

new_time_data = data_change_Time(obsdata=obsdata, simdata=simdata)

obs = pd.read_excel(new_time_data['obsdata'])
sim = pd.read_excel(new_time_data['simdata'])

domain = {
    '北':['鞍部', '淡水站', '竹子湖', '基隆', '台北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳'],
    '中':['梧棲', '台中', '日月潭', '阿里山', '嘉義', '玉山'],
    '南':['嘉義', '玉山', '永康', '台南', '高雄', '大武', '恆春'],
    '雲嘉':['台中', '日月潭', '阿里山', '嘉義', '玉山', '永康', '台南'],
    '東部':['台中', '花蓮', '日月潭', '阿里山', '玉山', '成功', '台東', '大武'],
    '中雲嘉':['梧棲', '台中', '日月潭', '阿里山', '嘉義', '玉山', '永康', '台南'],
    '全台':['鞍部', '淡水站', '竹子湖', '基隆', '台北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '梧棲',
                '台中', '花蓮', '日月潭', '阿里山', '嘉義', '玉山', '成功', '永康', '台南', '台東', '高雄', '大武', '恆春'],
}

# for area,ston in domain.items():
#     print(ston)

# area = {
#     '北':10,
#     '中':6,
#     '南':7,
#     '雲嘉':7,
#     '東部':8,
#     '中雲嘉':8,
#     '全台':24,
# }

stons = []
for item in sim:
    stons.append(item)
stons.pop(0)

MBE = {ston: 0 for ston in stons}
MBE['overal'] = 0
# for ston in stons:
#     sim_hr_num=0
#     print('Processing'+ston)
#     for i in range(0,len(obs['GMT00    GMT08'])):
#         for j in range(0,len(sim['times'])):
#             if (obs['GMT00    GMT08'][i]==sim['times'][j]) and (float(obs[ston][i]) < 999.) and (float(sim[ston][j]) < 999.):
#                 sim_hr_num += 1 #總共模擬的小時
#                 sim_all_hr_num += 1
#                 tmp=sim[ston][j]-obs[ston][i] #if float(obs[ston][i])<999. else 999.
#                 MBE[ston] += tmp

#                 MBE['overal'] += tmp

#     if (sim_hr_num != 0):
#         MBE[ston] = MBE[ston]/(sim_hr_num)
#     else:
#         MBE[ston] = None
#     # print(ston+''+'MBE='+str(MBE[ston]))

for ston in stons:
    sim_hr_num=0
    print('Processing'+ston)
    for i in range(0,len(obs['GMT00    GMT08'])):
        if (obs['GMT00    GMT08'][i]==sim['times'][i]) and (float(obs[ston][i]) < 999.) and (float(sim[ston][i]) < 999.):
            sim_hr_num += 1 #總共模擬的小時
            tmp=sim[ston][i]-obs[ston][i] 
            MBE[ston] += tmp

            MBE['overal'] += tmp

    if (sim_hr_num != 0):
        MBE[ston] = MBE[ston]/(sim_hr_num)
    else:
        MBE[ston] = None

MBE['overal'] = MBE['overal']/(24*sim_hr_num)
print(sim_all_hr_num)
print(MBE)

# pd_MBE = pd.DataFrame(MBE)
# MBE.to_excel('全台.xlsx', index=False)

# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('全台.xlsx', engine='openpyxl')

# Convert the dataframe to an XlsxWriter Excel object.
# pd_MBE.to_excel(writer, sheet_name='工作表1')

# Close the Pandas Excel writer and output the Excel file.
# writer.save()






print('finish')
