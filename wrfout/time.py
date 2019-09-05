import netCDF4 as nc
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from netCDF4 import Dataset, num2date
import datetime
import time

filename = "wrfout_d04_2016-06-02_22_00_00"
ele_array = np.zeros((24,17))

print(len(ele_array[:,1]))

time=filename[11:24]
time=(datetime.datetime.strptime(time,'%Y-%m-%d_%H'))#.strftime('%Y-%m-%d-%H')
# a=0
for i in range(0,1+len(ele_array[:,1])):
    print(time)
    time=time+datetime.timedelta(hours=1)
    
