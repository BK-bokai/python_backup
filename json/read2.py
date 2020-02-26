import urllib.request as request
import urllib
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



filename=input("請輸入要儲存檔案名稱，ex:201601.csv : ")
start=input("請輸入起始時間(年-月-日-時)，ex:2019-10-10-12 : ")
end=input("請輸入結束時間(年-月-日-時)，ex:2019-10-10-14 : ")

# start = '2019-10-10-14'
# end = '2019-10-10-15'
# filename = "test.csv"

logfile = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".log"

try:
    datestart = datetime.datetime.strptime(start, '%Y-%m-%d-%H')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d-%H')
except BaseException:
    print("你輸入的日期有誤")


datas = []


while datestart <= dateend:
    print('正在抓取'+datestart.strftime('%Y-%m-%d-%H')+'的資料') 
    try:
        src = 'https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-001178?filters=Abbr%20eq%20%27%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E4%B8%AD%E7%99%BC%E9%9B%BB%E5%BB%A0%27%20and%20M_Time%20eq%20%27' +\
            datestart.strftime('%Y-%m-%d') + \
            '%20' + \
            datestart.strftime('%H') + \
            ':00:00%27&sort=M_Time&offset=0&limit=1000'
        
        with request.urlopen(src) as response:
            data = json.load(response)

            datas += data["result"]["records"]
 
    except BaseException:

        cmd = 'echo'+" "+ datestart.strftime('%Y-%m-%d-%H')+"沒資料"+" "+">>"+" "+logfile
        retcode = subprocess.call(cmd, shell=True) 
        if retcode != 0: sys.exit(retcode)
             
    

    datestart += datetime.timedelta(hours = 1)



with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Epb", "CNO", "Abbr", "PolNo", "ItemDesc","Item", "M_Time", "M_Val", "Std", "Unit", "Code2", "Std_s", "Code2Desc"])
    for datalist in datas:
        writer.writerow([datalist['Epb'], datalist['CNO'],datalist['Abbr'],
          datalist['PolNo'], datalist['ItemDesc'], datalist['Item'],
          datalist['M_Time'], datalist['M_Val'],
          datalist['Std'], datalist['Unit'], datalist['Code2'],
          datalist['Std_s'], datalist['Code2Desc']])
