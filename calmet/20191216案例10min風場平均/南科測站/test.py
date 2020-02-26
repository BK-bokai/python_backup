import datetime
import time
import numpy as np
import pandas as pd
import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import math

WD=360
WS=2.3


# u_tmp = 2*WS * \
#     math.cos(((270.-WD)/180.)*3.14159)  # u10
# v_tmp = 2*WS * \
#     math.sin(((270.-WD)/180.)*3.14159)  # v10

# ws_tmp = math.sqrt(math.pow(u_tmp, 2)+math.pow(v_tmp, 2))
# if (abs(u_tmp) <= 0.001) and (v_tmp > 0):
#     ddir = 90.
# elif (abs(u_tmp) <= 0.001) and (v_tmp < 0):
#     ddir = 270.
# elif (u_tmp > 0):
#     ddir = math.atan(v_tmp/u_tmp)*57.2957795
# elif (u_tmp < 0):
#     ddir = math.atan(v_tmp/u_tmp)*57.2957795+180.0
#     wd_tmp = 270.-ddir
# if wd_tmp < 0:
#     wd_tmp += 360
# elif wd_tmp > 360:
#     wd_tmp -= 360


u_tmp = WS * math.cos((270 - WD) * math.pi / 180)

v_tmp = WS * math.sin((270 - WD) * math.pi / 180)
if u_tmp > 0 and v_tmp > 0:
    wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
elif u_tmp < 0 and v_tmp > 0:
    wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
elif u_tmp < 0 and v_tmp < 0:
    wd_tmp = 90 - math.atan(v_tmp / u_tmp) * 180 / math.pi
elif u_tmp > 0 and v_tmp < 0:
    wd_tmp = 270 - math.atan(v_tmp / u_tmp) * 180 / math.pi
elif u_tmp == 0 and v_tmp > 0:
    wd_tmp = 180
elif u_tmp == 0 and v_tmp < 0:
    wd_tmp = 0
elif u_tmp > 0 and v_tmp == 0:
    wd_tmp = 270
elif u_tmp < 0 and v_tmp == 0:
    wd_tmp = 90
elif u_tmp == 0 and v_tmp == 0:
    wd_tmp = 9999

ws_tmp = math.sqrt(math.pow(u_tmp, 2)+math.pow(v_tmp, 2))


