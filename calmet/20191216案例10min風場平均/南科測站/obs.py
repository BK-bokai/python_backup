import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook


start = '2019-12-16-00:00'
end = '2019-12-17-23:50'
filename = 'g29_1081216-1081218_min.xlsx'
obs = pd.read_excel(filename)
ston = 'g29'

time_key = {}
title = ['時間', 'WS', 'WD', 'ICELL', 'ICC', 'AT', 'RH', 'P', '天氣型態']

time_key['titie'] = title
datestart = datetime.datetime.strptime(start, '%Y-%m-%d-%H:%M')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d-%H:%M')

data = {
    'WS': obs['WS'],
    'WD': obs['WD'],
    'AT': obs['AT'],
    'times': []
}

for i in range(0, len(obs['時間'])):
    data['times'].append(datetime.datetime.strptime(obs['日期'][i].strftime(
        '%Y-%m-%d')+' '+obs['時間'][i].strftime('%H:%M:%S'), '%Y-%m-%d %H:%M:%S'))


while(datestart <= dateend):
        if(datestart in data['times']):
                index=data['times'].index(datestart)
                # WDtmp = obs['WD'][index] if obs['WS'][index]>0.3 else 9999 #排除靜風
                tmp_data=[obs['WS'][index],obs['WD'][index],9999,9999,obs['AT'][i]+273.15,9999,9999,9999]
                time_key[datestart]=tmp_data

        else:
                time_key[datestart]=[9999,9999,9999,9999,9999,9999,9999,9999]


        datestart+=datetime.timedelta(minutes=10)


wb = Workbook()
ws = wb.active
ws.title = ston
ws.append(title)
i=0
for key, value in time_key.items() :
        if(i==0):
                i+=1
                continue
        i+=1
        ws.append([key]+value)
# 儲存成 create_sample.xlsx 檔案
wb.save(ston+'.xlsx')
