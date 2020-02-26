import math
import datetime
import time
import jd_module
from jd_module import d_to_jd


def Zenith_angle(lat, day):

    # date = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
    date = day

    m = int(date.strftime('%m'))
    d = int(date.strftime('%d'))
    h = int(date.strftime('%H'))

    pi = math.pi
    arc2dgr = 180. / pi
    dgr2arc = pi / 180.

    tile = 23.5*(pi/180)*math.sin((30*(m-1)+d-81) * (pi/180))
    cosZ = math.sin(lat*dgr2arc)*math.sin(tile)+math.cos(lat *
                                                         dgr2arc)*math.cos(tile)*math.cos((pi/12)*(h-12))
    return math.acos(cosZ)*arc2dgr


# lat = 23.10729
# day = "2019-12-16 12:00:00"

# print(Zenith_angle(day=day, lat=lat))
