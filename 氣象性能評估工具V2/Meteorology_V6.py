#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
import os
import re, time
import xlsxwriter
import datetime
from lib.data_change_Time import data_change_Time
from lib.txt_To_xlsx import txt_To_xlsx
from lib.evaluate_T2_V2 import evaluate_T2
from lib.MergeTxt_obs import MergeTxt_obs
from lib.MergeTxt_sim import MergeTxt_sim


start = input("請輸入起始時間，ex:2016-01-01 : ")
end = input("請輸入結束時間，ex:2016-02-01 : ")

now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
workdir = "D:\\bokai\\python\\python-code\\氣象性能評估工具V2\\result\\"+now+"_"+start+"-"+end
if not os.path.isdir(workdir):
    os.mkdir(workdir)


obsfile= MergeTxt_obs(start=start,end=end,workdir=workdir)
simfile= MergeTxt_sim(start=start,end=end,workdir=workdir)

# print(obsfile.split('\\')[-1].split('.')[0])
T2_eva = evaluate_T2(obsfile=obsfile,simfile=simfile,workdir=workdir)


# 创建工作簿
workbook = xlsxwriter.Workbook(workdir+'//'+start+'_'+end+'_evaluate_T2.xlsx')
for area,stons in T2_eva['domain'].items():
    # 创建工作表
    worksheet = workbook.add_worksheet(area)
    worksheet.write(0, 1, 'MBE')
    worksheet.write(0, 2, 'MAGE')
    for i in range(len(stons)):
        
        MBE_item = T2_eva['MBE'][area][stons[i]]
        MAGE_item = T2_eva['MAGE'][area][stons[i]]

        worksheet.write(i+1, 0, stons[i])
        worksheet.write(i+1, 1, MBE_item)  # 第一個參數是列，第二個是行
        worksheet.write(i+1, 2, MAGE_item)

        worksheet.write(len(stons), 0, 'overal')
        worksheet.write(len(stons), 1, T2_eva['MBE'][area]['overal'])
        worksheet.write(len(stons), 2, T2_eva['MAGE'][area]['overal'])

workbook.close()








print('finish')
