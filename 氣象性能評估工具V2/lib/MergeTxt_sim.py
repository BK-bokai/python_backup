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
import datetime
from lib.data_change_Time import data_change_Time
from lib.txt_To_xlsx import txt_To_xlsx
import glob
import sys


def MergeTxt_sim(start,end,workdir):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    start -= datetime.timedelta(days=1)
    end += datetime.timedelta(days=1)
    filetimes = []
    while (start <= end):
        filetime = start.strftime('%Y-%m-%d')
        filetimes.append(filetime)
        start += datetime.timedelta(days=1)
    newfile = 'wrfout_d04_'+filetimes[0]+'_'+filetimes[-1]+'_T2.txt'
    outputFile = open(workdir+'\\'+newfile,"a+")
    for i in range(0,len(filetimes)):
        inputFile = open("D:\\bokai\\python\\python-code\\氣象性能評估工具V2\\data\\newsim\\wrfout_d04_"+filetimes[i]+"_T2.txt")
        outputFile.write(inputFile.read())
    
    return newfile
    



def raw_MergeTxt_sim():
    start = datetime.datetime.strptime('2016-06-01', '%Y-%m-%d')
    end = datetime.datetime.strptime('2016-06-30', '%Y-%m-%d')
    while (start <= end):
        filetime = start.strftime('%Y-%m-%d')
        outputFile = open('D:\\bokai\\python\\python-code\\氣象性能評估工具\\data\\newsim\\wrfout_d04_'+filetime+'_T2.txt',"a+")
        for txtFile in (glob.glob('D:\\bokai\\python\\python-code\\氣象性能評估工具\\data\\sim\\wrfout_d04_'+filetime+'*.txt')):
            inputFile = open(txtFile)
            outputFile.write(inputFile.read())
        start += datetime.timedelta(days=1)


    

# outputFile = open('D:\\bokai\\python\\python-code\\氣象性能評估工具\\data\\newsim\\wrfout_d04_2016-06-30_00_00_00.txt',"a+")
# for txtFile in glob.glob('D:\\bokai\\python\\python-code\\氣象性能評估工具\\data\\sim\\wrfout_d04_2016-06-30*.txt'):
#     inputFile = open(txtFile)
#     outputFile.write(inputFile.read())






 

 
 




