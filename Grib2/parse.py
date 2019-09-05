import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from netCDF4 import Dataset, num2date
filename = "20181101.nc"
nc = Dataset(filename, 'r', Format='NETCDF4')
var=nc.variables.keys()
t2=np.array(nc.variables['t2m'])
lat=nc.variables['latitude']
lon=nc.variables['longitude']


m=Basemap(projection='cyl',llcrnrlat=15,urcrnrlat=55,llcrnrlon=70,urcrnrlon=140,resolution='l')
lons,lats=m.makegrid(71,41)
lats=lats[::-1]

x,y=m(lons,lats)
m.drawparallels(np.arange(15.,56.,10.),labels=[1,0,0,0],fontsize=15)
m.drawmeridians(np.arange(75.,141.,15.),labels=[0,0,0,1],fontsize=15)
m.drawlsmask()
curve=m.contour(lons,lats,t2,colors='k')
shade=m.contourf(lons,lats,t2)
m.colorbar(shade)
plt.clabel(curve,fmt='%1.0f')
# print(t2)
# time = nc.variables['time']
# unit = time.units
# dates = num2date (time[:], units=unit, calendar='365_day')

# # get coordinates variables
# lats = nc.variables['latitude'][:]
# lons = nc.variables['longitude'][:]

# # sfc= nc.variables['Min_SFC'][:]
# times = nc.variables['time'][:]

# # convert date, how to store date only strip away time?
# print ("Converting Dates")
# units = nc.variables['time'].units
# dates = num2date (times[:], units=units, calendar='365_day')

# #print [dates.strftime('%Y%m%d%H') for date in dates]

# header = ['Latitude', 'Longitude']

# # append dates to header string

# for d in dates:
#     print (d)
#     header.append(d)

# # write to file
# import csv

# with open('Output.csv', 'wb') as csvFile:
#     outputwriter = csv.writer(csvFile, delimiter=',')
#     outputwriter.writerow(header)
#     for lat, lon in zip(lats, lons):
#       outputwriter.writerow( [lat, lon] )
 
# # close the output file
# csvFile.close()
# # close netcdf
# nc.close()