import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import sys
import re
import time
import xlsxwriter
import datetime
import numpy as np



def is_number(num):
    is_float = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    is_int = re.compile(r'^[-+]?\d+$')
    flost_result = is_float.match(num)
    int_tesult = is_int.match(num)
    if flost_result or int_tesult:
        return True
    else:
        return False


SO2 = {
    'LTS': [],
}


start = datetime.datetime.strptime('2016-01-01-00', '%Y-%m-%d-%H')
end   = datetime.datetime.strptime('2016-12-31-23', '%Y-%m-%d-%H')
while start <= end:
    SO2['LTS'].append(start.strftime('%Y-%m-%d-%H'))
    start += datetime.timedelta(hours=1)

airDataDir=os.path.dirname(os.path.abspath(__file__)) + '\\105_HOUR_00_20170301'
files = os.listdir(airDataDir)
for dirs in files:
    airDataDir_sub = airDataDir + '\\' + dirs
    datas = os.listdir(airDataDir_sub)
    for data in datas:
        if data.find('xls') > 1:
            dataFile = airDataDir_sub + '\\' + data
            SO2[data[4:7]]=[]

            for i in range(len(SO2['LTS'])):
                SO2[data[4:7]].append(999)

        

            obs = pd.read_excel(dataFile, header=None)
            obs = obs.values.tolist()

            for dayList in obs:
                if 'SO2' in dayList:
                    # 判斷是否為數字
                    for i in range(3, len(dayList)):
                        if is_number(str(dayList[i])) != True:
                            dayList[i] = 999
                    # 移除測站index
                    del dayList[1]
                    del dayList[1]
                    for i in range(len(dayList)-1):
                        obsTime = datetime.datetime.strptime(dayList[0]+'/'+str(i), '%Y/%m/%d/%H')
                        obsTime = obsTime.strftime('%Y-%m-%d-%H')
                        if(obsTime in SO2['LTS']):
                            index=SO2['LTS'].index(obsTime)
                            SO2[data[4:7]][index] = dayList[i+1]
                        print(data[4:7],obsTime)

data=pd.DataFrame(SO2)
data.to_excel('test.xls',index=False)


# obs = pd.read_excel(
#     "C:\\Bokai\\python_code\\空品性能評估工具\\105_HOUR_00_20170301\\105年 中部空品區\\105年二林站_20170217.xls", header=None)
# obs = obs.values.tolist()

# for dayList in obs:
#     if 'SO2' in dayList:
#         # 判斷是否為數字
#         for i in range(3, len(dayList)):
#             if is_number(str(dayList[i])) != True:
#                 dayList[i] = 999
#         # 移除測站index
#         del dayList[0]
#         del dayList[0]
#         del dayList[0]
#         SO2['二林站']+=dayList
# data=pd.DataFrame(SO2)
# data.to_excel('test.xls',index=False)
