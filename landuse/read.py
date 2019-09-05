# from openpyxl import load_workbook
# wb = load_workbook('category.xlsx')  #載入一個工作簿
# print (wb)         #獲取各個sheet的名字
# # ws2 = wb.get_sheet_by_name("工作表1")
# # print(ws2)

import pandas as pd
df = pd.read_excel("category.xlsx")
i=0
category=[]
for key, value in df.items() :
    i=i+1
    category.append(key)
    # print (i,key)
# df.head(15)
# cfile = open('category.xlsx','rb')
# data = cfile.read()
print(category[7])
print(category[9:14])
print(category[26:38])
print(category[54:60])
print(category[61:100])
print(category[101:104])
print(category[105])
print(category[107])
print(category[109:111])
print(category[125])