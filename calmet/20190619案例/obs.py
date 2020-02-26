import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook


start='2019-06-18-00:00'
end=  '2019-06-21-00:00'
time_key={}
title=['時間','WS','WD','ICELL','ICC','AT','RH','P','天氣型態']
# time_key['titie']=','.join(title)
time_key['titie']=title
datestart=datetime.datetime.strptime(start,'%Y-%m-%d-%H:%M')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d-%H:%M')
obs = pd.read_excel("永康20190618-20.xlsx")


# print(len(obs['時間']))

# for i in range(0,len(obs['時間'])):
#         print (obs['時間'][i])


while(datestart < dateend):
        # time_key[datestart]=(','.join([str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999")]))
        time_key[datestart]=([str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999")])

        for i in range(0,len(obs['時間'])):
                if (datestart==datetime.datetime.strptime(obs['時間'][i],'%Y-%m-%d-%H')):
                        data=[str(obs['WS'][i]),str(obs['WD'][i]),str(obs['ICELL'][i]),str(obs['ICC'][i]),str(obs['AT'][i]+273.15),str(obs['RH'][i]),str(obs['P'][i]),str(obs['天氣型態'][i])]
                        # data= ','.join(data)
                        time_key[datestart]=data


        if(float(time_key[datestart][6])==9999):
                time_key[datestart][6] = time_key[datestart-datetime.timedelta(minutes=10)][6]
                time_key[datestart][5] = time_key[datestart-datetime.timedelta(minutes=10)][5]

        
        datestart+=datetime.timedelta(minutes=10)
        
for key, value in time_key.items() :
        time_key[key]=','.join(time_key[key])

for key, value in time_key.items() :
        print (key)
        print (value)

# wb = Workbook()
# ws = wb.active
# ws.title = "永康"
# for key, value in time_key.items() :
#         # writer.writerow([key,str(value)])
#         ws.append([key,str(value)])
# # 儲存成 create_sample.xlsx 檔案
# wb.save('永康.xlsx')


# # ele_array = np.zeros( (len(hrlen),17))