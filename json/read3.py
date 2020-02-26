import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import re
import json
import subprocess, sys
import os
# src = 'http://175.98.139.88/tpaq/Webservice_SimEnvi/getData.aspx?Type=TPAQ&QueryTime=2019-07-31&token=sPmfGnfEHB8u6bQNIDbsOC3kSgGoSCSN'
# filename=input("請輸入要儲存檔案名稱，ex:201601.csv : ")
# start=input("請輸入起始時間，ex:2016-01-01 : ")
# end=input("請輸入結束時間，ex:2016-02-01 : ")

start = '2019-03-01'
end = '2019-10-31'
filename="ts01.csv"
logfile = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".log"
try:
    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
except BaseException:
    print ("你輸入的日期有誤")



datas = []

while datestart <= dateend:
    print(datestart)
    try:
        src = 'http://ts01.gi-tech.com.tw/tpaq/Webservice_SimEnvi/getData.aspx?Type=CEMS_air_fromEPA&QueryTime=' + \
            datestart.strftime('%Y-%m-%d') + \
            '&token=sPmfGnfEHB8u6bQNIDbsOC3kSgGoSCSN'

        # print(src)
        with request.urlopen(src) as response:
            data = json.load(response)

            datas += data
    
            # datas.append(data)

    except BaseException:

        cmd = 'echo'+" "+ datestart.strftime('%Y-%m-%d')+"沒資料"+" "+">>"+" "+logfile
        retcode = subprocess.call(cmd, shell=True) 
        if retcode != 0: sys.exit(retcode)

# print(data)
# for key in data:
#     print(key)


# for datalist in data:
#     print(datalist['M_Time'], datalist['PolNo'],
#           datalist['ItemDesc'], datalist['M_Val'], datalist['Code2Desc'])

    datestart += datetime.timedelta(days=1)


with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["M_Time", "PolNo", "ItemDesc", "M_Val", "Code2Desc"])
    for datalist in datas:
        writer.writerow([datalist['M_Time'], datalist['PolNo'],
                        datalist['ItemDesc'], datalist['M_Val'], datalist['Code2Desc']])
# tmp=[]
# for datalist in datas:
#     # a += 1
#     tmp+=datalist['M_Time']
#     # print(datalist['M_Time'])

# print(datas[:]['M_Time'])
