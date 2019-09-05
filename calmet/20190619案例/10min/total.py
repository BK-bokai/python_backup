import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import jd_module
from jd_module import d_to_jd


start='2019-06-18-00:00'
end=  '2019-06-21-00:00'
time_key={}
title=['時間','WS','WD','ICELL','ICC','AT','RH','P','天氣型態']
time_key['titie']=','.join(title)
datestart=datetime.datetime.strptime(start,'%Y-%m-%d-%H:%M')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d-%H:%M')

nk  = pd.read_excel("南科.xlsx")
g29 = pd.read_excel("g29.xlsx")
g13 = pd.read_excel("g13.xlsx")
g19 = pd.read_excel("g19.xlsx")
sh  = pd.read_excel("善化.xlsx")
uk  = pd.read_excel("永康.xlsx")



# print(len(obs['時間']))

# for i in range(0,len(obs['時間'])):
#         print (obs['時間'][i])

wb = Workbook()
ws = wb.active
ws.title = "total"
startMin=0
while(datestart < dateend):
       
#         ws.append([datestart])
        for i in range(0,len(nk['時間'])):
                if (datestart==datetime.datetime.strptime(str(nk['時間'][i]),'%Y-%m-%d %H:%M:%S')):

                        jultmp=str(d_to_jd(str(nk['時間'][i])))

                        startDay=int(jultmp[4:7])
                        endDay  =int(jultmp[4:7])

                        startHr=int(str(nk['時間'][i])[10:13])
                        endHr=int(str(nk['時間'][i])[10:13])

                        if (startMin>3000):
                                startMin=0
                        endMin=startMin+600

                        if(endMin==3600 and endHr == 23 ):
                                endHr == 0
                                endDay += 1

                        if (endMin==3600):
                                endMin=0
                                endHr += 1

                        if (endHr==24):
                                endHr=0
                        
                        ws.append([str(jultmp[0:4]),str(startDay),str(startHr),str(startMin),str(jultmp[0:4]),str(endDay),str(endHr),str(endMin)])
                        ws.append([str(nk['WS'][i]),str(nk['WD'][i]),str(nk['ICELL'][i]),str(nk['ICC'][i]),str(nk['AT'][i]),str(nk['RH'][i]),str(nk['P'][i]),str(nk['天氣型態'][i])])
                        ws.append([str(g29['WS'][i]),str(g29['WD'][i]),str(g29['ICELL'][i]),str(g29['ICC'][i]),str(g29['AT'][i]),str(g29['RH'][i]),str(g29['P'][i]),str(g29['天氣型態'][i])])
                        ws.append([str(g13['WS'][i]),str(g13['WD'][i]),str(g13['ICELL'][i]),str(g13['ICC'][i]),str(g13['AT'][i]),str(g13['RH'][i]),str(g13['P'][i]),str(g13['天氣型態'][i])])
                        ws.append([str(g19['WS'][i]),str(g19['WD'][i]),str(g19['ICELL'][i]),str(g19['ICC'][i]),str(g19['AT'][i]),str(g19['RH'][i]),str(g19['P'][i]),str(g19['天氣型態'][i])])
                        ws.append([str(sh['WS'][i]),str(sh['WD'][i]),str(sh['ICELL'][i]),str(sh['ICC'][i]),str(sh['AT'][i]),str(sh['RH'][i]),str(sh['P'][i]),str(sh['天氣型態'][i])])
                        ws.append([str(uk['WS'][i]),str(uk['WD'][i]),str(uk['ICELL'][i]),str(uk['ICC'][i]),str(uk['AT'][i]),str(uk['RH'][i]),str(uk['P'][i]),str(uk['天氣型態'][i])])
                        startMin +=600
                        
        datestart+=datetime.timedelta(minutes=10)
#         ws.append([datestart])
        
# # for key, value in time_key.items() :
# #         print (key)
# #         print (value)


wb.save('total.xlsx')


# # ele_array = np.zeros( (len(hrlen),17))