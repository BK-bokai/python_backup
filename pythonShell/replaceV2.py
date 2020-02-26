# -*- coding: UTF-8 -*-
import subprocess, sys
import re
import os

filePath = 'D:\\bokai\\劉博凱_景丰\\calmet\\20190619南科案例\\模擬結果\\plot.BAS'


fp3=open(filePath,"r")
fp4=open("test.BAS","w")
 
for s in fp3.readlines():#先读出来
    step1= s.replace("年","2019") 
    step2= step1.replace("月","06")
    step3= step2.replace("日","19")
    step4= step3.replace("時","16")
    step5= step4.replace("分","20")
    fp4.write(step5)

fp3.close()
fp4.close()









