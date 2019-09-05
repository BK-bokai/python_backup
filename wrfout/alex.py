import netCDF4 as nc
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from netCDF4 import Dataset, num2date
import datetime
import time

#for j in range(0,3):
filename = "wrfout_d0"+str(1)+"_2016-10-01_00_00_00"
data = Dataset(filename, 'r', Format='NETCDF4')
var=data.variables.keys()
# print(var)
rain=np.array(data.variables['RAINC'][:])+np.array(data.variables['RAINNC'][:])
lat=np.array(data.variables['XLAT'])
lon=np.array(data.variables['XLONG'])
# print(var)
print(lon.shape)
minLon = np.min(lon[:,:,:])
maxLon = np.max(lon[:,:,:])
minLat = np.min(lat[:,:,:])
maxLat = np.max(lat[:,:,:])
print(minLon,maxLon,minLat,maxLat)

#------------------------------------
time=filename[11:24]
startime=(datetime.datetime.strptime(time,'%Y-%m-%d_%H'))
endtime=(datetime.datetime.strptime("2016-10-02_23",'%Y-%m-%d_%H'))
# time_L=len(rain[:,1,1])
# print(time_L,time)
#---------------------------------------

#設定clormap
nws_precip_colors = [
    '#fdfdfd',
    '#ccccb3',
    '#99ffff',
    '#66b3ff',
    '#0073e6',
    '#002699',
    '#009900',
    '#1aff1a',
    '#ffff00',
    '#ffcc00',
    '#ff9900',
    '#ff0000',
    '#cc0000',
    '#990000',
    '#800040',
    '#b30047',
    '#ff0066',
    '#ff80b3' ]
precip_colormpa = matplotlib.colors.ListedColormap(nws_precip_colors)

NX=lon[:]
NY=lat[:]
lx=len(NX)
ly=len(NY)

#minx,miny=min(NX),min(NY)
#maxx,maxy=max(NX),max(NY)
i=0
while startime<=endtime:
     # #設定地圖
    plt.close('all')
    fig = plt.figure(figsize=(20,20))
    #for i in range(5,11,1):

    #plt.subplot(3,2,i-4)
    m= Basemap(projection='cyl',resolution='h',llcrnrlat=minLat,urcrnrlat=maxLat,llcrnrlon=minLon,urcrnrlon=maxLon) #給設定要畫的經緯度範圍

    #plot setting
    cLevel=[0,0.5,1,2,6,10,15,20,30,40,50,70,90,110,130,150,200,300,400]
    norm  =matplotlib.colors.BoundaryNorm(cLevel,18)
    # #換算網格
    lons, lats = m.makegrid(lx, ly)#將經緯度換算成網格點數
    x, y = m(lons, lats)


    # #畫海岸線
    m.drawcoastlines()
    #
    # #畫等值線
    m.contourf(lon[0,:,:],lat[0,:,:],rain[i,:,:],
            cmap=precip_colormpa,alpha=0.65,
            norm=norm,levels=cLevel,linestytles=None  )
    #
    m.drawparallels(np.arange(minLon,maxLon,1.),labels=[1,0,0,0],fontsize=15)#畫緯度線[1,0,0,0]分別代表左,右,上,下，故這邊意思是在左邊給標示N
    m.drawmeridians(np.arange(minLat,maxLat,1.),labels=[0,0,0,1],fontsize=15)#畫經度線
    plt.colorbar()
    plt.title('T='+startime.strftime('%Y-%m-%d-%H'))
    plt.show()
    #----------------------------------------------------
    startime=startime+datetime.timedelta(hours=1)
    i=i+1
#
#
