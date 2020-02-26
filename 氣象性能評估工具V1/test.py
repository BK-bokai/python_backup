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
from lib.evaluate_T2 import evaluate_T2
from lib.MergeTxt_obs import MergeTxt_obs
from lib.MergeTxt_sim import MergeTxt_sim


start = input("請輸入起始時間，ex:2016-01-01 : ")
end = input("請輸入結束時間，ex:2016-02-01 : ")

now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
workdir = "D:\\bokai\\python\\python-code\\氣象性能評估工具\\result\\"+now+"_"+start+"-"+end
if not os.path.isdir(workdir):
    os.mkdir(workdir)


obsfile= MergeTxt_obs(start=start,end=end,workdir=workdir)
simfile= MergeTxt_sim(start=start,end=end,workdir=workdir)
print(obsfile.split('\\')[-1].split('.')[0])
# T2_eva = evaluate_T2(obsfile=obsfile,simfile=simfile,workdir=workdir)

# simdata = txt_To_xlsx(filename='371_MODIS_UCM_T2_201606.txt')
# # obsdata = '201606obs.xlsx'
# obsfile='201606_T2_obs.xlsx'
# simfile='371_MODIS_UCM_T2_201606.txt'
# T2_eva = evaluate_T2(obsfile=obsfile,simfile=simfile)

# # 创建工作簿
# workbook = xlsxwriter.Workbook(obsfile[0:6]+'T2.xlsx')
# for area,stons in T2_eva['domain'].items():
#     # 创建工作表
#     worksheet = workbook.add_worksheet(area)
#     worksheet.write(0, 1, 'MBE')
#     worksheet.write(0, 2, 'MAGE')
#     for i in range(len(stons)):
#         worksheet.write(i+1, 0, stons[i])
#         MBE_item = T2_eva['MBE'][area][stons[i]]
#         MAGE_item = T2_eva['MAGE'][area][stons[i]]
#         worksheet.write(i+1, 1, MBE_item)  # 第一個參數是列，第二個是行
#         worksheet.write(i+1, 2, MAGE_item)
# workbook.close()








print('finish')
