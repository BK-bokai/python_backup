import CWB_WD_module
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

# print("#馬祖")
# T467990=CWB_WD_module.cwbdata(str('467990'),start,end)
# print(times.shape,T467990.shape,hrnum)
#彭佳嶼
# T466950=CWB_WD_module.cwbdata(str('466950'),start,end)
print("#鞍部")
WD466910=CWB_WD_module.cwbdata(str('466910'),start,end)
print("#淡水")
WD466900=CWB_WD_module.cwbdata(str('466900'),start,end)
print("#竹子湖")
WD466930=CWB_WD_module.cwbdata(str('466930'),start,end)
print("#基隆")
WD466940=CWB_WD_module.cwbdata(str('466940'),start,end)
print("#臺北")
WD466920=CWB_WD_module.cwbdata(str('466920'),start,end)
print("#新屋")
WD467050=CWB_WD_module.cwbdata(str('467050'),start,end)
print("#板橋")
WD466880=CWB_WD_module.cwbdata(str('466880'),start,end)
print("#新竹")
WD467571=CWB_WD_module.cwbdata(str('467571'),start,end)
print("#宜蘭")
WD467080=CWB_WD_module.cwbdata(str('467080'),start,end)
print("#蘇澳")
WD467060=CWB_WD_module.cwbdata(str('467060'),start,end)
# print("#金門")
# T467110=CWB_WD_module.cwbdata(str('467110'),start,end)
print("#梧棲")
WD467770=CWB_WD_module.cwbdata(str('467770'),start,end)
print("#台中")
WD467490=CWB_WD_module.cwbdata(str('467490'),start,end)
print("#花蓮")
WD466990=CWB_WD_module.cwbdata(str('466990'),start,end)
print("#日月潭")
WD467650=CWB_WD_module.cwbdata(str('467650'),start,end)
# print("#澎湖")
# T467350=CWB_WD_module.cwbdata(str('467350'),start,end)
print("#阿里山")
WD467530=CWB_WD_module.cwbdata(str('467530'),start,end)
print("#嘉義")
WD467480=CWB_WD_module.cwbdata(str('467480'),start,end)
print("#玉山")
WD467550=CWB_WD_module.cwbdata(str('467550'),start,end)
# print("#東吉")
# T467300=CWB_WD_module.cwbdata(str('467300'),start,end)
# print("#七股")
print("#成功")
WD467610=CWB_WD_module.cwbdata(str('467610'),start,end)
print("#永康")
WD467420=CWB_WD_module.cwbdata(str('467420'),start,end)
print("#台南")
WD467410=CWB_WD_module.cwbdata(str('467410'),start,end)
print("#台東")
WD467660=CWB_WD_module.cwbdata(str('467660'),start,end)
print("#高雄")
WD467440=CWB_WD_module.cwbdata(str('467440'),start,end)
print("#大武")
WD467540=CWB_WD_module.cwbdata(str('467540'),start,end)
# print("#蘭嶼")
# T467620=CWB_WD_module.cwbdata(str('467620'),start,end)
print("#恆春")
WD467590=CWB_WD_module.cwbdata(str('467590'),start,end)
# print(T466880.shape)
# print(times.shape)
# print(hrnum)

# print(T466880[1])
with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
#     # 1.直接寫出-標題
    writer.writerow(['times','馬祖','彭佳嶼','鞍部','淡水','竹子湖','基隆','臺北','新屋','板橋','新竹','宜蘭','蘇澳','金門','梧棲','台中','花蓮','日月潭','澎湖','阿里山','嘉義','玉山','東吉島','七股','成功','永康','台南','台東','高雄','大武','蘭嶼','恆春'])
    for k in range(0,int(hrnum)):
        writer.writerow([times[k],"999.9","999.9",WD466910[k],WD466900[k],WD466930[k],WD466940[k],WD466920[k],WD467050[k],WD466880[k],WD467571[k],WD467080[k],WD467060[k],"999.9",WD467770[k],WD467490[k],WD466990[k],WD467650[k],"999.9",WD467530[k],WD467480[k],WD467550[k],"999.9",'999.9',WD467610[k],WD467420[k],WD467410[k],WD467660[k],WD467440[k],WD467540[k],"999.9",WD467590[k]])
