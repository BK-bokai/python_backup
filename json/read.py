import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import re
import json
src = 'http://175.98.139.88/tpaq/Webservice_SimEnvi/getData.aspx?Type=TPAQ&QueryTime=2019-07-31&token=sPmfGnfEHB8u6bQNIDbsOC3kSgGoSCSN'


with request.urlopen(src) as response:
    data = json.load(response)

# for datalist in data:
#     print(datalist['SiteID'],datalist['sampledate'],datalist['AT'],datalist['PM25'],datalist['SO2'],datalist['O3'],datalist['NO2'],datalist['NOx'],datalist['NO'],datalist['TEMP'],datalist['RH'],datalist['RF'],datalist['WS'],datalist['WD'])


with open("filename", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["SiteID","sampledate","AT","PM25","SO2","O3","NO2","NOx","NO","TEMP","RH","RF","WS","WD"])
    for datalist in data:
        writer.writerow([datalist['SiteID'],datalist['sampledate'],datalist['AT'],datalist['PM25'],datalist['SO2'],datalist['O3'],datalist['NO2'],datalist['NOx'],datalist['NO'],datalist['TEMP'],datalist['RH'],datalist['RF'],datalist['WS'],datalist['WD']])