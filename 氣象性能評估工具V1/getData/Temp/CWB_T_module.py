def cwbdata(sta,start,end):
    import urllib.request as request
    from bs4 import BeautifulSoup
    import numpy as np
    import csv
    import datetime
    import time
    import calendar
    import re

    # sta='467571'
    # start='2016-02-02'
    # end='2016-02-03'
        
    datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
    dateend=datetime.datetime.strptime(end,'%Y-%m-%d')

    hrnum=((datetime.datetime.strptime(end,'%Y-%m-%d')-datetime.datetime.strptime(start,'%Y-%m-%d')).days*24)+24
    # print(hr,type(hr),type(24))
    hrlen = np.zeros( (int(hrnum)))
    hr=[] 
    StnPres=[]
    SeaPres=[]
    T=[]   

    check = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    while datestart<=dateend:
            
        print(datestart.strftime('%Y-%m-%d'))
        elements = []
        ele_array = []
          
        src='http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station='+sta+'&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker='+datestart.strftime('%Y-%m-%d')
        with request.urlopen(src) as response:
            data=response.read().decode("utf-8")
            soup = BeautifulSoup(data, 'html.parser')
        data=soup.find_all('tr')
        error=soup.find_all('label')        
        error=error[0].get_text()
        if error !='本段時間區間內無觀測資料！':# and sta !=             
            for i in range(4,28):
                data[i-4]=data[i].get_text().strip("\n").split()
                elements.append(data[i-4])
                ele_array = np.array(elements)
                hr.append(ele_array[i-4,0])
                StnPres.append(ele_array[i-4,1])
                SeaPres.append(ele_array[i-4,2])
                T.append(ele_array[i-4,3])
        else:
                ele_array = []
                ele_array = np.zeros( (len(hrlen),17))
                ele_array[:,:] = 999.9
                T=np.array(ele_array[:,3])
                Td=np.array(ele_array[:,4])
                RH=np.array(ele_array[:,5])
                WS=np.array(ele_array[:,6])
                WD=np.array(ele_array[:,7])

        
        datestart+=datetime.timedelta(days=1)
    return (T)
    
    

        