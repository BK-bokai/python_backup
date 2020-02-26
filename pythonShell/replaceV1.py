# -*- coding: UTF-8 -*-
import subprocess, sys
import re
import os

filePath = 'D:\\bokai\\劉博凱_景丰\\calmet\\20190619南科案例\\模擬結果\\avg.BAS'

fp3=open(filePath,"r+") #不用w w会清空数据
s=fp3.read()#读出 
fp3.seek(0,0) #指针移到头  原来的数据还在 是替换 会存在一个问题 如果少   会替换不了全部数据，自已思考解决!!!
#从头写入
fp3.write(s.replace("20190619_0400","20190619_0600"))

fp3.close()









