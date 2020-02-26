# -*- coding: UTF-8 -*-
import subprocess, sys
import re
import os


scriptPath = '"C:\Program Files\Golden Software\Surfer 13\Scripter\Scripter.exe"'

# filePath = '"'+"D:"+"\/"+"bokai\劉博凱_景丰\calmet\/"+"20190619南科案例\模擬結果\Script1.BAS"+'"'
filePath = '"D:\/bokai\劉博凱_景丰\calmet\/20190619南科案例\模擬結果\/avg.BAS"'

cmd=scriptPath +" "+"-x"+" "+ filePath
# print (cmd)
retcode = subprocess.call(cmd, shell=True) 
if retcode != 0: sys.exit(retcode)
# cmd = "echo" + datestart.strftime('%Y-%m-%d-%H') + '沒資料'