import shapefile
# conda install pyshp if you can't import shapefile
sf = shapefile.Reader("台灣村里界_修正竹北及蘇澳_10203版_TWD97_town.shp")
shapes = sf.shapes()
print (type(shapes)) 

recds = sf.records()
for i in recds: 
    print (i[9])



# for record in sf.records():
#     HUC8s.append(record[sf.fields.index(['HUC8', 'C', 8, 0])-1])



