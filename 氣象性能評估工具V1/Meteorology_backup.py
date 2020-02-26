#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import re
import xlsxwriter

# col=[]
# obs = pd.read_excel("201606obs.xlsx")
# # sim = pd.read_excel("201607sim.xlsx")
# for item in obs:
#     col.append(item)

# sim = pd.read_csv('371_MODIS_UCM_T2_201606.txt',header=None, encoding='utf-8', delim_whitespace=True, index_col=0)
# sim = sim.values.tolist()
# sim = pd.read_csv('371_MODIS_UCM_T2_201606.csv', sep='\t', header=None)
# sim.columns = col


# try:
#     with open('371_MODIS_UCM_T2_201606.txt','r') as data:
#         sim = data.read()
#         xls=xlwt.Workbook()
# sim = sim.strip('][').split('\t')
# sim = sim.split('\t')

# # sim.pop(col)
# print(sim)
# def txt_xls(filename, xlsname):
#     """
#     :文本转换成xls的函数
#     :param filename txt文本文件名称、
#     :param xlsname 表示转换后的excel文件名
#     """
#     try:
#         with open(filename, 'r') as data:
#             xls = xlwt.Workbook()
#             # 生成excel的方法，声明excel
#             sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
#             index = ['times', '馬祖', '彭佳嶼', '鞍部', '淡水', '竹子湖', '基隆', '臺北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '金門', '梧棲', '台中', '花蓮', '日月潭', '澎湖', '阿里山', '嘉義', '玉山', '東吉島', '七股', '成功', '永康', '台南', '台東', '高雄', '大武', '蘭嶼', '恆春']
#             for i in range(len(index)):
#                 sheet.write(0, i, index[i])
#             x = 1
#             while True:
#                 # 按行循环，读取文本文件
#                 line = data.readline()
#                 if not line:
#                     break  # 如果没有内容，则退出循环
#                 for i in range(len(line.strip(' ').split(' '))):
#                     item = line.strip(' ').split(' ')[i]
#                     sheet.write(x, i, item)  # x单元格经度，i 单元格纬度
#                 x += 1  # excel另起一行

#             xls.save(xlsname)  # 保存xls文件
#     except:
#         raise


# if __name__ == "__main__":
#     filename = "371_MODIS_UCM_T2_201606.txt"
#     xlsname = "test.xls"
#     txt_xls(filename, xlsname)

# def txt_xls(filename, xlsname):
#     """
#     :文本转换成xls的函数
#     :param filename txt文本文件名称、
#     :param xlsname 表示转换后的excel文件名
#     """
#     try:
#         with open(filename, 'r') as data:
#             xls = xlwt.Workbook()
#             # 生成excel的方法，声明excel
#             sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
#             index = ['times', '馬祖', '彭佳嶼', '鞍部', '淡水', '竹子湖', '基隆', '臺北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '金門', '梧棲', '台中', '花蓮', '日月潭', '澎湖', '阿里山', '嘉義', '玉山', '東吉島', '七股', '成功', '永康', '台南', '台東', '高雄', '大武', '蘭嶼', '恆春']
#             for i in range(len(index)):
#                 sheet.write(0, i, index[i])
#             x = 1
#             while True:
#                 # 按行循环，读取文本文件
#                 line = data.readline()
#                 if not line:
#                     break  # 如果没有内容，则退出循环
#                 for i in range(len(re.split(r'\s+',line.strip(' ')))):
#                     item = re.split(r'\s+',line.strip(' '))[i]
#                     sheet.write(x, i, item)  # x单元格经度，i 单元格纬度
#                 x += 1  # excel另起一行

#             xls.save(xlsname)  # 保存xls文件
#     except:
#         raise


# if __name__ == "__main__":
#     filename = "371_MODIS_UCM_T2_201606.txt"
#     xlsname = "test.xlsx"
#     txt_xls(filename, xlsname)


# data = []
# index = ['times', '馬祖', '彭佳嶼', '鞍部', '淡水', '竹子湖', '基隆', '臺北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '金門', '梧棲',
#          '台中', '花蓮', '日月潭', '澎湖', '阿里山', '嘉義', '玉山', '東吉島', '七股', '成功', '永康', '台南', '台東', '高雄', '大武', '蘭嶼', '恆春']
# data.append(index)
# with open("371_MODIS_UCM_T2_201606.txt", 'r') as sim:
#     while True:
#         line = sim.readline()
#         if not line:
#             break  # 如果没有内容，则退出循环
#         data.append(re.split(r'\s+', line.strip(' ')))

# df = pd.DataFrame(data)

# df.to_excel('new.xlsx')


# 创建工作簿
workbook = xlsxwriter.Workbook("test2.xlsx")
    # 创建工作表
worksheet = workbook.add_worksheet('工作表1')
index = ['times', '馬祖', '彭佳嶼', '鞍部', '淡水', '竹子湖', '基隆', '臺北', '新屋', '板橋', '新竹', '宜蘭', '蘇澳', '金門', '梧棲',
            '台中', '花蓮', '日月潭', '澎湖', '阿里山', '嘉義', '玉山', '東吉島', '七股', '成功', '永康', '台南', '台東', '高雄', '大武', '蘭嶼', '恆春']
for i in range(len(index)):
    worksheet.write(0, i, index[i])
x = 1
with open ("371_MODIS_UCM_T2_201606.txt", 'r') as data:
    while True:
        # 按行循环，读取文本文件
        line = data.readline()
        if not line:
            break  # 如果没有内容，则退出循环
        for i in range(len(re.split(r'\s+', line.strip(' ')))):
            item = re.split(r'\s+', line.strip(' '))[i]
            worksheet.write(x, i, item)  # x单元格经度，i 单元格纬度
        x += 1  # excel另起一行
    workbook.close()

