import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import math


start = '2019-12-16-00:00'
end = '2019-12-17-23:50'
filename = '南科1081216-1081218_min.xlsx'
obs = pd.read_excel(filename)
ston = '南科實中'

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
        datestart_10 = datestart-datetime.timedelta(minutes=9)
        i = 0
        u_tmp = 0
        v_tmp = 0
        ws_tmp = 0
        wd_tmp = 0
        while(datestart_10 <= datestart):
                if(datestart_10 in data['times']):
                        index = data['times'].index(datestart_10)
                        if obs['WS'][index] != 9999 and obs['WD'][index] != 9999 and obs['WS'][index] != -999 and obs['WD'][index] != -999:
                                i += 1
                                u_tmp += obs['WS'][index] * math.cos((270 - obs['WD'][index]) * math.pi / 180)
                                v_tmp += obs['WS'][index] * math.sin((270 - obs['WD'][index]) * math.pi / 180)
                datestart_10 += datetime.timedelta(minutes=1)

        if(i != 0):
                u_tmp = u_tmp/i
                v_tmp = v_tmp/i
                ws_tmp = math.sqrt(math.pow(u_tmp,2)+math.pow(v_tmp,2))

                if u_tmp > 0 and v_tmp > 0:
                        wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
                elif u_tmp < 0 and v_tmp > 0:
                        wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
                elif u_tmp < 0 and v_tmp < 0:
                        wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
                elif u_tmp > 0 and v_tmp < 0:
                        wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
                elif u_tmp == 0 and v_tmp > 0:
                        wd_tmp = 180
                elif u_tmp == 0 and v_tmp < 0:
                        wd_tmp = 0
                elif u_tmp > 0 and v_tmp == 0:
                        wd_tmp = 270
                elif u_tmp < 0 and v_tmp == 0:
                        wd_tmp = 90
                elif u_tmp == 0 and v_tmp == 0:
                        wd_tmp = 9999
        elif(i == 0):
                ws_tmp = 9999
                wd_tmp = 9999
        
        if ws_tmp <=0.2:
                wd_tmp = 9999
                ws_tmp = 9999

        if(datestart in data['times']):
                index=data['times'].index(datestart)
                # WDtmp = obs['WD'][index] if obs['WS'][index]>0.3 else 9999 #排除靜風
                tmp_data=[ws_tmp,wd_tmp,9999,9999,obs['AT'][i]+273.15,9999,9999,9999]
                time_key[datestart]=tmp_data
        else:
                time_key[datestart]=[9999,9999,9999,9999,9999,9999,9999,9999]

        datestart += datetime.timedelta(minutes=10)


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
