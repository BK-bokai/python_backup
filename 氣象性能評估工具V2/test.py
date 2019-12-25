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


li1 = ['A','A B', 'C']
print('A B' in li1)


print('finish')
