import CWB_R_module
import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import pandas as pd


filename=input("請輸入要儲存檔案名稱，ex:201601.csv : ")
start=input("請輸入起始時間，ex:2016-01-01 : ")
end=input("請輸入結束時間，ex:2016-02-01 : ")
# filename="2016.csv"
# start='2016-05-28'
# end='2016-6-3'



hrnum=((datetime.datetime.strptime(end,'%Y-%m-%d')-datetime.datetime.strptime(start,'%Y-%m-%d')).days*24)+24

starthr=str(start)+'-01'
endhr=str(end)+'-00'

datestarthr=datetime.datetime.strptime(starthr,'%Y-%m-%d-%H')
dateendhr=datetime.datetime.strptime(endhr,'%Y-%m-%d-%H')+datetime.timedelta(days=1)

times=[]
while datestarthr<=dateendhr:
    times.append(str(datestarthr))
    datestarthr=datestarthr+datetime.timedelta(hours=1)
times=np.array(times[:])    


print("#三義")
RC0E530=CWB_R_module.cwbdata(str('C0E530'),start,end)
print("#銅鑼")
RC0E780=CWB_R_module.cwbdata(str('C0E780'),start,end)
print("#南湖")
RC1E691=CWB_R_module.cwbdata(str('C1E691'),start,end)
print("#通霄")
RC0E590=CWB_R_module.cwbdata(str('C0E590'),start,end)

print("#竹南")
RC0E420=CWB_R_module.cwbdata(str('C0E420'),start,end)
print("#頭份")
RC0E730=CWB_R_module.cwbdata(str('C0E730'),start,end)
print("#高鐵苗栗")
RC0E870=CWB_R_module.cwbdata(str('C0E870'),start,end)
print("#苗栗")
RC0E750=CWB_R_module.cwbdata(str('C0E750'),start,end)

print("#明德")
RC0E550=CWB_R_module.cwbdata(str('C0E550'),start,end)
print("#公館")
RC1A730=CWB_R_module.cwbdata(str('C1A730'),start,end)
print("#後龍")
RC0E540=CWB_R_module.cwbdata(str('C0E540'),start,end)
print("#新竹市東區")
RC0D660=CWB_R_module.cwbdata(str('C0D660'),start,end)

with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
#     # 1.直接寫出-標題
    writer.writerow(['times','三義','銅鑼','南湖','通霄','竹南','頭份','高鐵苗栗','苗栗','明德','公館','後龍','新竹市東區'])
    for k in range(0,int(hrnum)):
        writer.writerow([times[k],RC0E530[k],RC0E780[k],RC1E691[k],RC0E590[k],RC0E420[k],RC0E730[k],RC0E870[k],RC0E750[k],RC0E550[k],RC1A730[k],RC0E540[k],RC0D660[k]])
