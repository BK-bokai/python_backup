import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from netCDF4 import Dataset, num2date
filename = "20181101.nc"
data = Dataset(filename, 'r', Format='NETCDF4')
var=data.variables.keys()
t2=np.array(data.variables['t2m'][:])
lat=data.variables['latitude']
lon=data.variables['longitude']
print(var)
print(t2.shape)
NX=lon[:]
NY=lat[:]
lx=len(NX)
ly=len(NY)

minx,miny=min(NX),min(NY)
maxx,maxy=max(NX),max(NY)


#設定地圖
fig = plt.figure()
m= Basemap(projection='cyl',resolution='h',llcrnrlat=21.5,urcrnrlat=25.4,llcrnrlon=119,urcrnrlon=123)#給設定要畫的經緯度範圍

#換算網格
lons, lats = m.makegrid(lx, ly)#將經緯度換算成網格點數
x, y = m(lons, lats)


#畫海岸線
m.drawcoastlines()

#畫等值線
m.contour(x,y,t2[3,:,:])

m.drawparallels(np.arange(21.5,25.,1.),labels=[1,0,0,0],fontsize=15)#畫緯度線[1,0,0,0]分別代表左,右,上,下，故這邊意思是在左邊給標示N
m.drawmeridians(np.arange(119,123,1.),labels=[0,0,0,1],fontsize=15)#畫經度線

plt.show()


plt.show()