import urllib.request as request
from bs4 import BeautifulSoup
import numpy as np
import csv
import datetime
import time
import calendar
import pandas as pd

sta_data = pd.read_csv('station.csv')
sta = sta_data['station']
start='2016-05-31'
end='2016-06-03'
# print(str(sta_str[1])+str(sta_str[2]))
hrnum=((datetime.datetime.strptime(end,'%Y-%m-%d')-datetime.datetime.strptime(start,'%Y-%m-%d')).days*24)+24
# print(hr,type(hr),type(24))
hrlen = np.zeros( (int(hrnum)))
print(len(hrlen))

with open('A.csv', 'w', newline='') as csvFile:
    for x in sta:
        
            
        datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
        dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
        hr=[]
        

        while datestart<=dateend:
            
            
            elements = []
            ele_array = []
            src='http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station='+str(x)+'&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker='+datestart.strftime('%Y-%m-%d')
            with request.urlopen(src) as response:
                data=response.read().decode("utf-8")

            soup = BeautifulSoup(data, 'html.parser')
            data=soup.find_all('tr')
            error=soup.find_all('label')
            error=error[0].get_text()
            if error !='本段時間區間內無觀測資料！':# and x !=467571:
                print("data exit")
            
                
                for i in range(4,28):
                    data[i-4]=data[i].get_text().strip("\n").split()
                    elements.append(data[i-4])    
            
                    ele_array = np.array(elements)
                    # print(ele_array[i-4,0])
                    hr.append(ele_array[i-4,0])
                   
                # WSGust=np.array(ele_array[:,8])
                # WDGust=np.array(ele_array[:,9])
                # Precp=np.array(ele_array[:,10])
                # PrecpHour=np.array(ele_array[:,11])
                # SunShine=np.array(ele_array[:,12])
                # GloblRad=np.array(ele_array[:,13])
                # Visb=np.array(ele_array[:,14])
                # UVI=np.array(ele_array[:,15])
                # Cloud_Amount=np.array(ele_array[:,16])
                # print(str(x))
                # print(T)
            # elif error !='本段時間區間內無觀測資料！' and x ==467571:
            #     for i in range(4,28):
            #         data[i-4]=data[i].get_text().strip("\n").split()
            #         elements.append(data[i-4])
            #     ele_array = np.array(elements)#.reshape(24, 17)
            #     hr=np.array(ele_array[:,0])
            #     StnPres=np.array(ele_array[:,1])
            #     SeaPres=np.array(ele_array[:,2])
            #     T=np.array(ele_array[:,3])
            #     Td=np.array(ele_array[:,4])
            #     RH=np.array(ele_array[:,5])
            #     WS=np.array(ele_array[:,6])
            #     WD=np.array(ele_array[:,7])
            #     WSGust=np.array(ele_array[:,8])
            #     WDGust=np.array(ele_array[:,9])
            #     Precp=np.array(ele_array[:,10])
            #     PrecpHour=np.array(ele_array[:,11])
            #     SunShine=np.array(ele_array[:,12])
            #     GloblRad=np.array(ele_array[:,13])
            #     Visb=np.array(ele_array[:,14])
            #     UVI=np.zeros( (len(hrlen),1) )
            #     UVI[:,0]=999.
            #     Cloud_Amount=np.array(ele_array[:,15])
                # print(str(x))
                # print(T)

            else:
                ele_array = []
                # ele_array = np.array(ele_array)
                ele_array = np.zeros( (len(hrlen),17))
                ele_array[:,:] = 999.9
                hr=np.array(ele_array[:,0])
                StnPres=np.array(ele_array[:,1])
                SeaPres=np.array(ele_array[:,2])
                T=np.array(ele_array[:,3])
                Td=np.array(ele_array[:,4])
                RH=np.array(ele_array[:,5])
                WS=np.array(ele_array[:,6])
                WD=np.array(ele_array[:,7])
                # WSGust=np.array(ele_array[:,8])
                # WDGust=np.array(ele_array[:,9])
                # Precp=np.array(ele_array[:,10])
                # PrecpHour=np.array(ele_array[:,11])
                # SunShine=np.array(ele_array[:,12])
                # GloblRad=np.array(ele_array[:,13])
                # Visb=np.array(ele_array[:,14])
                # UVI=np.array(ele_array[:,15])
                # Cloud_Amount=np.array(ele_array[:,16]) 
                print(error)
                # print(str(x))
                # print(T)
            
            datestart+=datetime.timedelta(days=1)
        print(str(x))  
        print(datestart.strftime('%Y-%m-%d'))
        print(hr)
    # # print(data[0,1])
    
    # writer = csv.writer(csvFile)
    # #    1.直接寫出-標題
    # writer.writerow(['time','STATION'])
    # writer.writerow(str(datestart)+str(hr),T[:,:])