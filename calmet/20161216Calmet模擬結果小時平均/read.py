import subprocess
import sys
import re
import os
import glob
import pandas as pd
from pandas.core.frame import DataFrame
import datetime
import math
from openpyxl import load_workbook
from openpyxl import Workbook

start = '2019-12-16-04:00'
end = '2019-12-17-14:00'
ston = 'g19'
datestart = datetime.datetime.strptime(start, '%Y-%m-%d-%H:%M')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d-%H:%M')
time_key = {}
out_data = {
    'date':[],
    'year':[],
    'month':[],
    'day':[],
    'hr':[],
    'ws':[],
    'wd':[],
}

new_data = {
    'date':[],
    'u':[],
    'v':[],
}

for input_data in (glob.glob('模擬結果\*')):
    data = pd.read_csv(input_data,header = None)
    date = datetime.datetime.strptime(input_data.split('\\')[-1][0:13], '%Y%m%d_%H%M')
    for i in range(len(data[0])):
        X = data[0][i].split()[0]
        Y = data[0][i].split()[1]
        U = float(data[0][i].split()[2])
        V = float(data[0][i].split()[3])        
        if abs(float(X)-175020) < 150 and abs(float(Y)-2558056) < 150 and dateend>date>datestart:
            new_data['date'].append(date)
            new_data['u'].append(U)
            new_data['v'].append(V)

while(datestart <= dateend):
    datestart_hr = datestart-datetime.timedelta(minutes=50)
    u_tmp = 0
    v_tmp = 0
    ws_tmp = 0
    wd_tmp = 0
    i =0
    while(datestart_hr <= datestart):
        if(datestart_hr in new_data['date']):
            i+=1
            index = new_data['date'].index(datestart_hr)
            u_tmp += new_data['u'][index]
            v_tmp += new_data['v'][index]
        datestart_hr += datetime.timedelta(minutes=10)
    if(i != 0):
        u_tmp = u_tmp/i
        v_tmp = v_tmp/i
        ws_tmp = math.sqrt(math.pow(u_tmp, 2)+math.pow(v_tmp, 2))

        if u_tmp > 0 and v_tmp > 0:
            wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
            wd_tmp += 180
        elif u_tmp < 0 and v_tmp > 0:
            wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
            wd_tmp += 180
        elif u_tmp < 0 and v_tmp < 0:
            wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
            wd_tmp += 180
        elif u_tmp > 0 and v_tmp < 0:
            wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
            wd_tmp += 180
        elif u_tmp == 0 and v_tmp > 0:
            wd_tmp = 180
            wd_tmp += 180
        elif u_tmp == 0 and v_tmp < 0:
            wd_tmp = 0
            wd_tmp += 180
        elif u_tmp > 0 and v_tmp == 0:
            wd_tmp = 270
            wd_tmp += 180
        elif u_tmp < 0 and v_tmp == 0:
            wd_tmp = 90
            wd_tmp += 180
        elif u_tmp == 0 and v_tmp == 0:
            wd_tmp = 0.0
    elif(i == 0):
        ws_tmp = 0.0
        wd_tmp = 0.0
    
    wd_tmp = wd_tmp if wd_tmp <= 360 else wd_tmp-360

    y = int(datestart.strftime('%Y')[2:4])
    m = int(datestart.strftime('%m'))
    d = int(datestart.strftime('%d'))
    h = int(datestart.strftime('%H'))
    time_key[datestart] = [y, m, d, h, ws_tmp, 
        wd_tmp, u_tmp, v_tmp]
    datestart += datetime.timedelta(minutes=60)
title = ['時間', '年', '月', '日', '時',  'WS', 'WD', 'U', 'V']

wb = Workbook()
ws = wb.active
ws.title = ston
ws.append(title)
j = 0
for key, value in time_key.items():
    if(j == 0):
        j += 1
        continue
    j += 1
    ws.append([key]+value)
# 儲存成 create_sample.xlsx 檔案
wb.save(ston+'.xlsx')

test = DataFrame(new_data)
test.to_csv('test.csv', sep='\t', index=False, header = None)