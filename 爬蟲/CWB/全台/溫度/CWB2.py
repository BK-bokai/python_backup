import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import pandas as pd
sta='466910'
# sta_data = pd.read_csv('station.csv')
# sta = sta_data['station']

# print(str(sta[1])+str(sta[2]))


start='2016-02-01'
end='2016-02-02'
 
datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
elements = []

while datestart<=dateend:
    datestart+=datetime.timedelta(days=1)
    print(datestart.strftime('%Y-%m-%d'))

    src='http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466910&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker='+start
    with request.urlopen(src) as response:
        data=response.read().decode("utf-8")

    soup = BeautifulSoup(data, 'html.parser')
    data=soup.find_all('tr')
    # data2=data.find_all('tr')
    # data=soup.find_all('tr')
    print("=================================================================================================")
    
    for i in range(4,28):
        data[i-4]=data[i].get_text().strip("\n").split()
        elements.append(data[i-4])
    file=sta+'.csv'


    ele_array = np.array(elements)#.reshape(24, 17)
    print(ele_array.shape)
# # print(data[0,1])
# with open(file, 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     # 1.直接寫出-標題
#     writer.writerow(['year','hr','StnPres','SeaPres','Temperature','Td dew point','RH','WS','WD','WSGust','WDGust','Precp','PrecpHour','SunShine','GloblRad','Visb','UVI','Cloud Amount'])
#     for i in range(0,24):
#         writer.writerow(['2016',data[i]])