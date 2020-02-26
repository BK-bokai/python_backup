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
O3_106 = workbook.sheet_by_index(6)
O3_107 = workbook.sheet_by_index(7)
O3_108 = workbook.sheet_by_index(8)

cell_00 = O3_106.cell_value(0, 2)  # 讀取第1列第2行資料
row0 = O3_106.row_values(0)  # 讀取第1列資料
nrows = O3_106.nrows  # 讀取行數

s_ston = []
n_ston = []
w_ston = []
e_ston = []

times = []

for i in range(nrows):  # 迴圈逐行列印
    if i == 0:  # 跳過第一行
        continue
    time = "".join(O3_106.row_values(i)[0:3])
    time = time.replace('月', '/')
    time = time.replace('日', '/')

    times.append('2017/'+time)

    s_ston.append(O3_106.row_values(i)[3])
    n_ston.append(O3_106.row_values(i)[4])
    w_ston.append(O3_106.row_values(i)[5])
    e_ston.append(O3_106.row_values(i)[6])


s_O3=np.zeros( ( int((nrows-1)/24),24 ),'U10')
# s_O3 = [[0 for i in range(24)] for j in range(int((nrows-1)/24))]
date = []

for i in range(0, int((nrows-1)/24)):
    for j in range(0, 24):
        # if type(s_ston[(i*24)+j]) != type(0.5) :
        #     s_ston[(i*24)+j]=-999
        s_O3[i,j]=str(s_ston[(i*24)+j])
        # s_O3[i][j] = str(s_ston[(i*24)+j])


for i in range(0, nrows-1, 24):
    date.append(times[i][0:10])
# print(s_O3)


# print(data)


with open('test.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["日期", "測站", "測項", "00", "01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
#     for datelist in date:
#         writer.writerow([s_O3[]])


    for i in range(0, int((nrows-1)/24)):
        # writer.writerow([date[i],'s',(','.join(s_O3[i]))])
        writer.writerow([date[i],'南站','O3',s_O3[i,0],s_O3[i,1],s_O3[i,2],
        s_O3[i,3],s_O3[i,4],s_O3[i,5],s_O3[i,6],s_O3[i,7],s_O3[i,8],
        s_O3[i,9],s_O3[i,10],s_O3[i,11],s_O3[i,12],s_O3[i,13],s_O3[i,14],s_O3[i,15],
        s_O3[i,16],s_O3[i,17],s_O3[i,18],s_O3[i,19],s_O3[i,20],s_O3[i,21],
        s_O3[i,22],s_O3[i,23]])