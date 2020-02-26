import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import math
from Zenith_angle_module import Zenith_angle
from check_stab import check_stab


start = '2019-12-10-00:00'
end = '2019-12-11-23:00'
filename = '南科1081210-1081212_min.xlsx'
obs = pd.read_excel(filename)
ston = '南科實中'

lat = 23.10729  # 南科實中
# lat = 23.106341 # 29
# lat = 23.09004  # 13
# lat = 23.122679 # 19

# 雲量 2019-12/11 12/12
cloud = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# # 雲量 2019-12/16 12/17
# cloud = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]


time_key = {}
title = ['時間', '年', '月', '日', '時',  'WS', 'WD', 'AT', '穩定度','天頂角']

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
count = 0
while(datestart <= dateend):
    datestart_hr = datestart-datetime.timedelta(minutes=59)
    i = 0
    j = 0
    u_tmp = 0
    v_tmp = 0
    ws_tmp = 0
    wd_tmp = 0
    at_tmp = 0


    while(datestart_hr <= datestart):
        if(datestart_hr in data['times']):
            index = data['times'].index(datestart_hr)
            if obs['WS'][index] != 9999 and obs['WD'][index] != 9999 and obs['WS'][index] != -999 and obs['WD'][index] != -999:
                i += 1
                u_tmp += obs['WS'][index] * \
                    math.cos((270 - obs['WD'][index]) * math.pi / 180)
                v_tmp += obs['WS'][index] * \
                    math.sin((270 - obs['WD'][index]) * math.pi / 180)
            if obs['AT'][index] != 9999 and obs['AT'][index] != -999:
                j += 1
                at_tmp += obs['AT'][index]
        datestart_hr += datetime.timedelta(minutes=1)

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

    if j != 0:
        at_tmp = at_tmp/j
    elif j == 0:
        at_tmp = 0.0

    if ws_tmp <= 0.2:
        wd_tmp = 0.0
        ws_tmp = 0.0

    wd_tmp = wd_tmp if wd_tmp <= 360 else wd_tmp-360

    y = int(datestart.strftime('%Y')[2:4])
    m = int(datestart.strftime('%m'))
    d = int(datestart.strftime('%d'))
    h = int(datestart.strftime('%H'))

    stab_tmp=check_stab(Zenith_angle(day=datestart, lat=lat), cloud[count], ws_tmp)
    time_key[datestart] = [y, m, d, h, round(ws_tmp, 4), round(
        wd_tmp, 4), round(at_tmp, 1), stab_tmp, Zenith_angle(day=datestart, lat=lat)]
    count += 1
    datestart += datetime.timedelta(minutes=60)


wb = Workbook()
ws = wb.active
ws.title = ston
ws.append(title)
i = 0
for key, value in time_key.items():
    if(i == 0):
        i += 1
        continue
    i += 1
    ws.append([key]+value)
# 儲存成 create_sample.xlsx 檔案
wb.save(ston+'.xlsx')


    