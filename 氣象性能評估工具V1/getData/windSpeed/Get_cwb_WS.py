import CWB_WS_module
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
# T467990=CWB_WS_module.cwbdata(str('467990'),start,end)
# print(times.shape,T467990.shape,hrnum)
#彭佳嶼
# T466950=CWB_WS_module.cwbdata(str('466950'),start,end)
print("#鞍部")
WS466910=CWB_WS_module.cwbdata(str('466910'),start,end)
print("#淡水")
WS466900=CWB_WS_module.cwbdata(str('466900'),start,end)
print("#竹子湖")
WS466930=CWB_WS_module.cwbdata(str('466930'),start,end)
print("#基隆")
WS466940=CWB_WS_module.cwbdata(str('466940'),start,end)
print("#臺北")
WS466920=CWB_WS_module.cwbdata(str('466920'),start,end)
print("#新屋")
WS467050=CWB_WS_module.cwbdata(str('467050'),start,end)
print("#板橋")
WS466880=CWB_WS_module.cwbdata(str('466880'),start,end)
print("#新竹")
WS467571=CWB_WS_module.cwbdata(str('467571'),start,end)
print("#宜蘭")
WS467080=CWB_WS_module.cwbdata(str('467080'),start,end)
print("#蘇澳")
WS467060=CWB_WS_module.cwbdata(str('467060'),start,end)
# print("#金門")
# T467110=CWB_WS_module.cwbdata(str('467110'),start,end)
print("#梧棲")
WS467770=CWB_WS_module.cwbdata(str('467770'),start,end)
print("#台中")
WS467490=CWB_WS_module.cwbdata(str('467490'),start,end)
print("#花蓮")
WS466990=CWB_WS_module.cwbdata(str('466990'),start,end)
print("#日月潭")
WS467650=CWB_WS_module.cwbdata(str('467650'),start,end)
# print("#澎湖")
# T467350=CWB_WS_module.cwbdata(str('467350'),start,end)
print("#阿里山")
WS467530=CWB_WS_module.cwbdata(str('467530'),start,end)
print("#嘉義")
WS467480=CWB_WS_module.cwbdata(str('467480'),start,end)
print("#玉山")
WS467550=CWB_WS_module.cwbdata(str('467550'),start,end)
# print("#東吉")
# T467300=CWB_WS_module.cwbdata(str('467300'),start,end)
# print("#七股")
print("#成功")
WS467610=CWB_WS_module.cwbdata(str('467610'),start,end)
print("#永康")
WS467420=CWB_WS_module.cwbdata(str('467420'),start,end)
print("#台南")
WS467410=CWB_WS_module.cwbdata(str('467410'),start,end)
print("#台東")
WS467660=CWB_WS_module.cwbdata(str('467660'),start,end)
print("#高雄")
WS467440=CWB_WS_module.cwbdata(str('467440'),start,end)
print("#大武")
WS467540=CWB_WS_module.cwbdata(str('467540'),start,end)
# print("#蘭嶼")
# T467620=CWB_WS_module.cwbdata(str('467620'),start,end)
print("#恆春")
WS467590=CWB_WS_module.cwbdata(str('467590'),start,end)
# print(T466880.shape)
# print(times.shape)
# print(hrnum)

# print(T466880[1])
with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
#     # 1.直接寫出-標題
    writer.writerow(['times','馬祖','彭佳嶼','鞍部','淡水','竹子湖','基隆','臺北','新屋','板橋','新竹','宜蘭','蘇澳','金門','梧棲','台中','花蓮','日月潭','澎湖','阿里山','嘉義','玉山','東吉島','七股','成功','永康','台南','台東','高雄','大武','蘭嶼','恆春'])
    for k in range(0,int(hrnum)):
        writer.writerow([times[k],"999.9","999.9",WS466910[k],WS466900[k],WS466930[k],WS466940[k],WS466920[k],WS467050[k],WS466880[k],WS467571[k],WS467080[k],WS467060[k],"999.9",WS467770[k],WS467490[k],WS466990[k],WS467650[k],"999.9",WS467530[k],WS467480[k],WS467550[k],"999.9",'999.9',WS467610[k],WS467420[k],WS467410[k],WS467660[k],WS467440[k],WS467540[k],"999.9",WS467590[k]])
