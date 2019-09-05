from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

 

#投影方法 map = Basemap() cyl是圓柱投影法
# map = Basemap(projection = 'cyl')
map = Basemap(projection='cyl',llcrnrlat=15,urcrnrlat=55,llcrnrlon=70,urcrnrlon=140,resolution='l')


map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'coral', lake_color = 'aqua')
map.drawcoastlines()
map.drawparallels(np.arange(-90., 91., 20.), labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(-180., 181., 40.), labels=[0,0,0,1], fontsize=10)


 

plt.show()