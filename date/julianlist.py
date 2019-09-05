import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook

# def d_to_jd(time):
#     fmt = '%Y.%m.%d.%H'
#     dt = datetime.strptime(time, fmt)
#     tt = dt.timetuple()
#     return tt.tm_year * 1000 + tt.tm_yday
# # x=0
# for x in range(0,23):
#     for y in range(0,3600,600) :
#         print( str(d_to_jd('2019.06.19.'+str(x))) + str(y) 
#         +' ' 
#         + str(d_to_jd('2019.06.19.' + str(x))) 
#         + str(y-600))

start='2019-06-18-00:00'
end=  '2019-06-21-00:00'
time_key={}
datestart=datetime.datetime.strptime(start,'%Y-%m-%d-%H:%M')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d-%H:%M')
yk = pd.read_excel("永康20190618-20.xlsx")

# print(len(yk['時間']))

# for i in range(0,len(yk['時間'])):
#         print (datetime.datetime.strptime(yk['時間'][i],'%Y-%m-%d-%H'))


while(datestart < dateend):
        time_key[datestart]=(','.join([str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999"),str("9999")]))
        # time_key[datestart]=["9999","9999","9999","9999","9999","9999","9999","9999"]
        for i in range(0,len(yk['時間'])):
                if (datestart==datetime.datetime.strptime(yk['時間'][i],'%Y-%m-%d-%H')):
                        # time_key[datestart]=np.array([yk['WS'][i],yk['WD'][i],yk['ICELL'][i],yk['ICC'][i],yk['AT'][i],yk['RH'][i],yk['P'][i],yk['天氣型態'][i]])
                        # time_key[datestart]=[yk['WS'][i],yk['WD'][i],yk['ICELL'][i],yk['ICC'][i],yk['AT'][i],yk['RH'][i],yk['P'][i],yk['天氣型態'][i]]
                        data=[str(yk['WS'][i]),str(yk['WD'][i]),str(yk['ICELL'][i]),str(yk['ICC'][i]),str(yk['AT'][i]),str(yk['RH'][i]),str(yk['P'][i]),str(yk['天氣型態'][i])]
                        data= ','.join(data)
                        # print(data)
                        time_key[datestart]=data

                        # time_key[datestart]=yk[:][i]
                        # print (time_key[datestart])
                
                        

        datestart+=datetime.timedelta(minutes=10)
        
for key, value in time_key.items() :
        print (key)
        print (value)
        # for i in value:
        #         print (i,end=', ')

# for i in time_key:
#     print(i,end=', ')#以逗号为分隔符


wb = Workbook()
ws = wb.active
# 指定值給 A1 儲存格
# 向下新增一列並連續插入值
ws.append(','.join(['時間','WS','WD','ICELL','ICC','AT','RH','P','天氣型態']))
for key, value in time_key.items() :
        # writer.writerow([key,str(value)])
        ws.append([key,str(value)])
# 儲存成 create_sample.xlsx 檔案
wb.save('create_sample.xlsx')


# ele_array = np.zeros( (len(hrlen),17))