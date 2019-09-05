import CWB_T_module
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
# T467990=CWB_T_module.cwbdata(str('467990'),start,end)
# print(times.shape,T467990.shape,hrnum)
#彭佳嶼
# T466950=CWB_T_module.cwbdata(str('466950'),start,end)
print("#鞍部")
T466910=CWB_T_module.cwbdata(str('466910'),start,end)
print("#淡水")
T466900=CWB_T_module.cwbdata(str('466900'),start,end)
print("#竹子湖")
T466930=CWB_T_module.cwbdata(str('466930'),start,end)
print("#基隆")
T466940=CWB_T_module.cwbdata(str('466940'),start,end)
print("#臺北")
T466920=CWB_T_module.cwbdata(str('466920'),start,end)
print("#新屋")
T467050=CWB_T_module.cwbdata(str('467050'),start,end)
print("#板橋")
T466880=CWB_T_module.cwbdata(str('466880'),start,end)
print("#新竹")
T467571=CWB_T_module.cwbdata(str('467571'),start,end)
print("#宜蘭")
T467080=CWB_T_module.cwbdata(str('467080'),start,end)
print("#蘇澳")
T467060=CWB_T_module.cwbdata(str('467060'),start,end)
# print("#金門")
# T467110=CWB_T_module.cwbdata(str('467110'),start,end)
print("#梧棲")
T467770=CWB_T_module.cwbdata(str('467770'),start,end)
print("#台中")
T467490=CWB_T_module.cwbdata(str('467490'),start,end)
print("#花蓮")
T466990=CWB_T_module.cwbdata(str('466990'),start,end)
print("#日月潭")
T467650=CWB_T_module.cwbdata(str('467650'),start,end)
# print("#澎湖")
# T467350=CWB_T_module.cwbdata(str('467350'),start,end)
print("#阿里山")
T467530=CWB_T_module.cwbdata(str('467530'),start,end)
print("#嘉義")
T467480=CWB_T_module.cwbdata(str('467480'),start,end)
print("#玉山")
T467550=CWB_T_module.cwbdata(str('467550'),start,end)
# print("#東吉")
# T467300=CWB_T_module.cwbdata(str('467300'),start,end)
# print("#七股")
print("#成功")
T467610=CWB_T_module.cwbdata(str('467610'),start,end)
print("#永康")
T467420=CWB_T_module.cwbdata(str('467420'),start,end)
print("#台南")
T467410=CWB_T_module.cwbdata(str('467410'),start,end)
print("#台東")
T467660=CWB_T_module.cwbdata(str('467660'),start,end)
print("#高雄")
T467440=CWB_T_module.cwbdata(str('467440'),start,end)
print("#大武")
T467540=CWB_T_module.cwbdata(str('467540'),start,end)
# print("#蘭嶼")
# T467620=CWB_T_module.cwbdata(str('467620'),start,end)
print("#恆春")
T467590=CWB_T_module.cwbdata(str('467590'),start,end)
# print(T466880.shape)
# print(times.shape)
# print(hrnum)

# print(T466880[1])
with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
#     # 1.直接寫出-標題
    writer.writerow(['times','馬祖','彭佳嶼','鞍部','淡水','竹子湖','基隆','臺北','新屋','板橋','新竹','宜蘭','蘇澳','金門','梧棲','台中','花蓮','日月潭','澎湖','阿里山','嘉義','玉山','東吉島','七股','成功','永康','台南','台東','高雄','大武','蘭嶼','恆春'])
    for k in range(0,int(hrnum)):
        writer.writerow([times[k],"999.9","999.9",T466910[k],T466900[k],T466930[k],T466940[k],T466920[k],T467050[k],T466880[k],T467571[k],T467080[k],T467060[k],"999.9",T467770[k],T467490[k],T466990[k],T467650[k],"999.9",T467530[k],T467480[k],T467550[k],"999.9",'999.9',T467610[k],T467420[k],T467410[k],T467660[k],T467440[k],T467540[k],"999.9",T467590[k]])
