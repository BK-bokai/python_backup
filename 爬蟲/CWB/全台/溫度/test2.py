import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar

 



# headers = {"User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
src='http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466850&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=2016-06-01'
with request.urlopen(src) as response:
    data=response.read().decode("utf-8")

soup = BeautifulSoup(data, 'html.parser')
error=soup.find_all('label')
error=error[0].get_text()
if error !='本段時間區間內無觀測資料！':
    print("data exit")
else:
    print(error)

    # data2=data.find_all('tr')
    # data=soup.find_all('tr')
    # print("=================================================================================================")
    # for i in range(4,28):
    #     data[i-4]=data[i].get_text().strip("\n").split()
    #     # data[i-4]=np.array(data[i].get_text())#.reshape(17,1)
    #     # print(data[i-4])
    #     # print(data[i].get_text())
    # file=sta+'-' + datestart.strftime('%Y-%m-%d')+ '.csv'
    # print(file)
    # # print(data[0,1])
    # with open(file, 'w', newline='') as csvFile:
    #     writer = csv.writer(csvFile)
    #     # 1.直接寫出-標題
    #     writer.writerow(['hr','StnPres','SeaPres','Temperature','Td dew point','RH','WS','WD','WSGust','WDGust','Precp','PrecpHour','SunShine','GloblRad','Visb','UVI','Cloud Amount'])
    #     for i in range(0,24):
    #         writer.writerow(data[i])
