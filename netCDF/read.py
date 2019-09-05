import os
import sys
# print(sys.path)
os.chdir('D:\\bokai\\python\\wgrib2')
# os.system("wgrib2")
# os.system(r"wgrib2 D:\\bokai\\python\\ncep\\fnl_20190124_12_00.grib2 -v")
os.system("wgrib2 D:\\bokai\\python\\ncep\\fnl_20190124_12_00.grib2 -crlf -s -d 260 -spread d.csv")
# os.system("wgrib2 D:\\bokai\\python\\ncep\\fnl_20190124_12_00.grib2 -d 260 -h -text -o test.txt") 
    #-d 260 -h -text -o 2m_tmp.txt")
# os.system(os.path.abspath('.')+'\wgrib\wgrib.exe 'fnl_20190124_12_00.grib2' -d 1 -text -nh -o 2m_tmp.txt')
