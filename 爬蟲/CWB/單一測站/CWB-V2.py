import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import re

sta='C0O900'
start='2019-06-17'
end='2019-06-18'
 
datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
totaldata=[]

while datestart<=dateend:
    
    # print(datestart.strftime('%Y-%m-%d'))


    

    # headers = {"User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    src='http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station='+sta+'&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker='+datestart.strftime('%Y-%m-%d')
    with request.urlopen(src) as response:
        data=response.read().decode("utf-8")
# s.encode("utf8").decode("cp950", "ignore")
    soup = BeautifulSoup(data, 'html.parser')
    data=soup.find_all('tr')
    # data2=data.find_all('tr')
    # data=soup.find_all('tr')
    # print("=================================================================================================")
    for i in range(4,28):
        # print(data[i].get_text())
        data[i-4]=(data[i].get_text()).split()
        # data[i-4]=data[i].get_text().strip("\n").split()
        # data[i-4]=np.array(data[i].get_text())#.reshape(17,1)
        # print(data[i-4])
        # print(data[i].get_text())
    file=sta+'-' + datestart.strftime('%Y-%m-%d')+ '.csv'
    print(file)
    # print(data[0,1])
    # with open(file, 'w', newline='') as csvFile:
    #     writer = csv.writer(csvFile)
    #     # 1.直接寫出-標題
    #     writer.writerow(['hr','StnPres','SeaPres','Temperature','Td dew point','RH','WS','WD','WSGust','WDGust','Precp','PrecpHour','SunShine','GloblRad','Visb','UVI','Cloud Amount'])
    #     for i in range(0,24):
    #         writer.writerow(data[i])
    datestart+=datetime.timedelta(days=1)
    totaldata.append(data)
totaldata = np.array(totaldata)
print(totaldata[0])

    


