import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook

def nk_obs_mudule(start,end,filename,ston):
        # start='2019-12-10-00:00'
        # end=  '2019-12-11-00:00'
        obs = pd.read_excel(filename)
        # ston = '永康'
        time_key={}
        title=['時間','WS','WD','ICELL','ICC','AT','RH','P','天氣型態']

        time_key['titie']=title
        datestart=datetime.datetime.strptime(start,'%Y-%m-%d-%H:%M')
        dateend=datetime.datetime.strptime(end,'%Y-%m-%d-%H:%M')




        while(datestart <= dateend):
                # time_key[datestart]=(','.join([str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999")]))
                time_key[datestart]=[9999,9999,9999,9999,9999,9999,9999,9999]

                for i in range(0,len(obs['時間'])):
                        if (datestart==datetime.datetime.strptime(obs['時間'][i],'%Y-%m-%d-%H')):
                                data=[obs['WS'][i],obs['WD'][i],obs['ICELL'][i],obs['ICC'][i],obs['AT'][i]+273.15,obs['RH'][i],obs['P'][i],obs['天氣型態'][i]]
                                time_key[datestart]=data

                if(float(time_key[datestart][6])==9999):
                        time_key[datestart][6] = time_key[datestart-datetime.timedelta(minutes=10)][6]
                        time_key[datestart][5] = time_key[datestart-datetime.timedelta(minutes=10)][5]

                
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

