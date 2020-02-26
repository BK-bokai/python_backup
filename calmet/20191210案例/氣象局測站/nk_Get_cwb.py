# from CWB_module import cwbdata
import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import pandas as pd
import xlsxwriter
from lib.CWB_module import cwbdata
from lib.nk_obs_mudule import nk_obs_mudule



start = '2019-12-10'
end = '2019-12-11'
ston = 'C0O900'#善化
ston_name = '善化'
# ston = '467420'#永康
# ston_name = '永康'


filename = ston+'_'+start+'_'+end[-2:]+'.xlsx'

hrnum = ((datetime.datetime.strptime(end, '%Y-%m-%d') -
          datetime.datetime.strptime(start, '%Y-%m-%d')).days*24)+24

# starthr = str(start)+'-01'
# endhr = str(end)+'-00'
starthr = str(start)+'-00'
endhr = str(end)+'-23'

datestarthr = datetime.datetime.strptime(starthr, '%Y-%m-%d-%H')
dateendhr = datetime.datetime.strptime(
    endhr, '%Y-%m-%d-%H')+datetime.timedelta(days=1)

times = []
year  = []
month = []
day   = []
hr    = []
ICELL = []
ICC   = []
weather_state=[]

while datestarthr <= dateendhr:
    times.append(datestarthr.strftime('%Y-%m-%d-%H'))
    year.append(int(datestarthr.strftime('%Y')))
    month.append(int(datestarthr.strftime('%m')))
    day.append(int(datestarthr.strftime('%d')))
    hr.append(datestarthr.strftime('%H:%M'))
    ICELL.append(9999)
    ICC.append(9999)
    weather_state.append(9999)

    datestarthr = datestarthr+datetime.timedelta(hours=1)
times = np.array(times[:])




WS = cwbdata(str(ston), start, end, 'WS')
WD = cwbdata(str(ston), start, end, 'WD')
AT = cwbdata(str(ston), start, end, 'T2')
RH = cwbdata(str(ston), start, end, 'RH')
P  = cwbdata(str(ston), start, end,'StnPres')

data = {
    '時間年': year,
    '時間月': month,
    '時間日': day,
    '時間時': hr,
    '時間':times,
    'WS': WS,
    'WD': WD,
    'ICELL':ICELL,
    'ICC':ICC,
    'AT':AT,
    'RH':RH,
    'P':P,
    '天氣型態':weather_state
}

workbook = xlsxwriter.Workbook(filename)
 # 创建工作表
worksheet = workbook.add_worksheet('工作表1')
i = 0
for index in data:
    worksheet.write(0, i, index)
    i += 1
for i in range(0, int(hrnum)):
    k = 0
    for j in data:
        worksheet.write(i+1, k, data[j][i])
        k += 1
workbook.close()


nk_obs_mudule(start=start+'-00:00',end=end+'-23:50',filename=filename,ston=ston_name)
