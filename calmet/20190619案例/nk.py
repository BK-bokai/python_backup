import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl

start='2019-06-17-00:00'
end=  '2019-06-23-00:00'
datestart=datetime.datetime.strptime(start,'%Y-%m-%d-%H:%M')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d-%H:%M')

    
wb = Workbook()
ws = wb.active
while(datestart < dateend):
        # time_key[datestart]=(','.join([str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999")]))
        # # time_key[datestart]=["9999","9999","9999","9999","9999","9999","9999","9999"]
        # for i in range(0,len(yk['時間'])):
        #         if (datestart==datetime.datetime.strptime(yk['時間'][i],'%Y-%m-%d-%H')):
        #                 # time_key[datestart]=np.array([yk['WS'][i],yk['WD'][i],yk['ICELL'][i],yk['ICC'][i],yk['AT'][i],yk['RH'][i],yk['P'][i],yk['天氣型態'][i]])
        #                 # time_key[datestart]=[yk['WS'][i],yk['WD'][i],yk['ICELL'][i],yk['ICC'][i],yk['AT'][i],yk['RH'][i],yk['P'][i],yk['天氣型態'][i]]
        #                 data=[str(yk['WS'][i]),str(yk['WD'][i]),str(yk['ICELL'][i]),str(yk['ICC'][i]),str(yk['AT'][i]),str(yk['RH'][i]),str(yk['P'][i]),str(yk['天氣型態'][i])]
        #                 data= ','.join(data)
        #                 # print(data)
        #                 time_key[datestart]=data

        #                 # time_key[datestart]=yk[:][i]
        #                 # print (time_key[datestart])

    # print(title)
    ws.append([datestart])
    # 儲存成 create_sample.xlsx 檔案

                
                        

    datestart+=datetime.timedelta(minutes=1)

wb.save('time.xlsx')