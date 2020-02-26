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


# newfilename = ".xlsx"
# 创建工作簿
workbook = xlsxwriter.Workbook('test.xlsx')

MBE_result = {}
MAGE_result = {}
for area,stons in domain.items():

    MBE = {ston: 0 for ston in stons}
    MBE['overal'] = 0

    MAGE = {ston: 0 for ston in stons}
    MAGE['overal'] = 0 

    sim_overal_hr = 0

    for ston in stons:
        sim_hr_num=0
        print('Processing'+ston)
        for i in range(0,len(obs['GMT00    GMT08'])):
            if (obs['GMT00    GMT08'][i]==sim['times'][i]) and (float(obs[ston][i]) < 999.) and (float(sim[ston][i]) < 999.):
                sim_hr_num += 1 #總共模擬的小時
                sim_overal_hr += 1

                tmp=sim[ston][i]-obs[ston][i] 
                MBE[ston] += tmp

                MBE['overal'] += tmp

                abstmp = abs(sim[ston][i]-obs[ston][i])
                MAGE[ston] += abstmp

                MAGE['overal'] += abstmp

        if (sim_hr_num != 0):
            MBE[ston] = MBE[ston]/(sim_hr_num)
            MAGE[ston] = MAGE[ston]/(sim_hr_num)
        else:
            MBE[ston] = None
            MAGE[ston] = None

    sim_overal_hr = sim_overal_hr/len(stons)

    MBE['overal'] = MBE['overal']/(len(stons)*sim_overal_hr)
    MAGE['overal'] = MAGE['overal']/(len(stons)*sim_overal_hr)

    MBE_result[area] = MBE
    MAGE_result[area] = MAGE


    


    # 创建工作表
    worksheet = workbook.add_worksheet(area)
    worksheet.write(0, 1, 'MBE')
    worksheet.write(0, 2, 'MAGE')
    for i in range(len(stons)):
        worksheet.write(i+1, 0, stons[i])
        MBE_item = MBE_result[area][stons[i]]
        MAGE_item = MAGE_result[area][stons[i]]
        worksheet.write(i+1, 1, MBE_item)  # 第一個參數是列，第二個是行
        worksheet.write(i+1, 2, MAGE_item)
workbook.close()

# print(len(MBE_result['北']))
# pd_MBE = pd.DataFrame(MBE)
# MBE.to_excel('全台.xlsx', index=False)

# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('全台.xlsx', engine='openpyxl')

# Convert the dataframe to an XlsxWriter Excel object.
# pd_MBE.to_excel(writer, sheet_name='工作表1')

# Close the Pandas Excel writer and output the Excel file.
# writer.save()






print('finish')
