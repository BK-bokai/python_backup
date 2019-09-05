#===================================================
#函式形式，呼叫cartopy，繪製區域地圖
#===================================================
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
def make_map(scale,box,xstep,ystep):
    fig=plt.figure(figsize=(8, 10))
    ax=plt.axes(projection=ccrs.PlateCarree())
    #set_extent需要配置相應的crs，否則出來的地圖範圍不準確
    ax.set_extent(box,crs=ccrs.PlateCarree())
    land = cfeature.NaturalEarthFeature('physical', 'land', scale,edgecolor='face',
                                                              facecolor=cfeature.COLORS['land'])
    ax.add_feature(land, facecolor='0.75')
    ax.coastlines(scale)
    #===================================================
    #影象地址D:\Program Files\WinPython-32bit-2.7.9.3\python-2.7.9\Lib\site-packages\
    #cartopy\data\raster\natural_earth\50-natural-earth-1-downsampled.png
    #如果有其它高精度影象檔案，改名替換即可
    ax.stock_img()
    #===================================================
    #標註座標軸
    ax.set_xticks(np.arange(box[0],box[1]+xstep,xstep), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(box[2],box[3]+ystep,ystep), crs=ccrs.PlateCarree())
    #zero_direction_label用來設定經度的0度加不加E和W
    lon_formatter = LongitudeFormatter(zero_direction_label=False)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #新增網格線
    ax.grid()
    return fig,ax
box=[100,150,0,50]
fig,ax=make_map(scale='50m',box=box,xstep=10,ystep=10)
plt.show()