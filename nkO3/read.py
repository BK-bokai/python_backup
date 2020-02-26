import xlwt
import xlrd
import pandas as pd
import numpy as np
import datetime
import time
import calendar
import csv

workbook = xlrd.open_workbook("南科CO_NO2_O3(106-108).xlsx")
# print(workbook.sheet_names())            #檢視所有sheet名稱
O3_data = workbook.sheet_by_index(6) #106
# O3_data = workbook.sheet_by_index(7) #107
# O3_data = workbook.sheet_by_index(8) #108
year = 2017


cell_00 = O3_data.cell_value(0, 2)  # 讀取第1列第2行資料
row0 = O3_data.row_values(0)  # 讀取第1列資料
nrows = O3_data.nrows  # 讀取行數

s_ston = []
n_ston = []
w_ston = []
e_ston = []

times = []

for i in range(nrows):  # 迴圈逐行列印
    if i == 0:  # 跳過第一行
        continue
    time = "".join(O3_data.row_values(i)[0:3])
    time = time.replace('月', '/')
    time = time.replace('日', '/')

    times.append(str(year)+'/'+time)

    s_ston.append(O3_data.row_values(i)[3])
    n_ston.append(O3_data.row_values(i)[4])
    w_ston.append(O3_data.row_values(i)[5])
    e_ston.append(O3_data.row_values(i)[6])

for i in range(0, nrows-1):    
    times[i]=datetime.datetime.strptime(times[i],'%Y/%m/%d/%H')
    times[i]=times[i].strftime('%Y/%m/%d')


s_O3=np.zeros( ( int((nrows-1)/24),24 ),'U10')
n_O3=np.zeros( ( int((nrows-1)/24),24 ),'U10')
w_O3=np.zeros( ( int((nrows-1)/24),24 ),'U10')
e_O3=np.zeros( ( int((nrows-1)/24),24 ),'U10')

for i in range(0, int((nrows-1)/24)):
    for j in range(0, 24):
        s_O3[i,j]=str(s_ston[(i*24)+j])
        n_O3[i,j]=str(n_ston[(i*24)+j])
        w_O3[i,j]=str(w_ston[(i*24)+j])
        e_O3[i,j]=str(e_ston[(i*24)+j])

# for i in range(0, nrows-1):    
#     times[i]=datetime.datetime.strptime(times[i],'%Y/%m/%d/%H')
#     times[i]=times[i].strftime('%Y/%m/%d')


date = []
for i in range(0, nrows-1, 24):
    date.append(times[i])


with open(str(year-1911)+'南站.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["日期", '測站', "測項", "00", "01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
    for i in range(0, int((nrows-1)/24)):
        writer.writerow([date[i],'南站','O3',s_O3[i,0],s_O3[i,1],s_O3[i,2],
        s_O3[i,3],s_O3[i,4],s_O3[i,5],s_O3[i,6],s_O3[i,7],s_O3[i,8],
        s_O3[i,9],s_O3[i,10],s_O3[i,11],s_O3[i,12],s_O3[i,13],s_O3[i,14],s_O3[i,15],
        s_O3[i,16],s_O3[i,17],s_O3[i,18],s_O3[i,19],s_O3[i,20],s_O3[i,21],
        s_O3[i,22],s_O3[i,23]])

with open(str(year-1911)+'北站.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["日期", '測站', "測項", "00", "01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
    for i in range(0, int((nrows-1)/24)):
        writer.writerow([date[i],'北站','O3',n_O3[i,0],n_O3[i,1],n_O3[i,2],
        n_O3[i,3],n_O3[i,4],n_O3[i,5],n_O3[i,6],n_O3[i,7],n_O3[i,8],
        n_O3[i,9],n_O3[i,10],n_O3[i,11],n_O3[i,12],n_O3[i,13],n_O3[i,14],n_O3[i,15],
        n_O3[i,16],n_O3[i,17],n_O3[i,18],n_O3[i,19],n_O3[i,20],n_O3[i,21],
        n_O3[i,22],n_O3[i,23]])

with open(str(year-1911)+'西站.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["日期", '測站', "測項", "00", "01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
    for i in range(0, int((nrows-1)/24)):
        writer.writerow([date[i],'西站','O3',w_O3[i,0],w_O3[i,1],w_O3[i,2],
        w_O3[i,3],w_O3[i,4],w_O3[i,5],w_O3[i,6],w_O3[i,7],w_O3[i,8],
        w_O3[i,9],w_O3[i,10],w_O3[i,11],w_O3[i,12],w_O3[i,13],w_O3[i,14],w_O3[i,15],
        w_O3[i,16],w_O3[i,17],w_O3[i,18],w_O3[i,19],w_O3[i,20],w_O3[i,21],
        w_O3[i,22],w_O3[i,23]])

with open(str(year-1911)+'東站.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["日期", '測站', "測項", "00", "01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
    for i in range(0, int((nrows-1)/24)):
        writer.writerow([date[i],'東站','O3',e_O3[i,0],e_O3[i,1],e_O3[i,2],
        e_O3[i,3],e_O3[i,4],e_O3[i,5],e_O3[i,6],e_O3[i,7],e_O3[i,8],
        e_O3[i,9],e_O3[i,10],e_O3[i,11],e_O3[i,12],e_O3[i,13],e_O3[i,14],e_O3[i,15],
        e_O3[i,16],e_O3[i,17],e_O3[i,18],e_O3[i,19],e_O3[i,20],e_O3[i,21],
        e_O3[i,22],e_O3[i,23]])


