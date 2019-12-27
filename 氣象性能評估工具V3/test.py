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


# obs_in = pd.read_excel("D:\\bokai\\python\\python-code\\氣象性能評估工具v2\\data\\obs\\2016-06-02_T2_obs.xlsx")
# obs_in = pd.read_excel("new_time_wrfout_d04_2016-06-04_2016-06-08_T2.xlsx")
# obs_in = pd.read_excel("D:\\bokai\\python\\python-code\\氣象性能評估工具V2\\result\\2019-12-26-09-45-46_2016-06-05-2016-06-07\\2016-06-05_2016-06-07_T2_obs.xlsx")


obs_in = pd.read_excel("2016-06-01_T2_obs.xlsx")


for time in obs_in['times']:
    print(time)