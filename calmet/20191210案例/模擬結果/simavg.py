import glob
import os
import subprocess, sys
import os

filePath = 'D:\\bokai\\python\\python-code\\calmet\\20191210案例\\模擬結果\\avg.BAS'


files = os.listdir("D:\\bokai\\python\\python-code\\calmet\\20191210案例\\模擬結果\\uv") 
for x in files:
    time=x.replace("uv.txt","")
    outfilepath='D:\\bokai\\python\\python-code\\calmet\\20191210案例\\模擬結果\\avgscript\\'+time+'.BAS'
    
    fp3=open(filePath,"r")
    fp4=open(outfilepath,"w")
 
    for s in fp3.readlines():#先读出来   
        fp4.write(s.replace("time",time)) #替换 并写入
    
    fp3.close()
    fp4.close()

    scriptPath = '"C:\Program Files\Golden Software\Surfer 13\Scripter\Scripter.exe"'
    executPath = '"D:\\bokai\\python\\python-code\\calmet\\20191210案例\\模擬結果\\avgscript\\'+time+'.BAS'+'"'

    cmd=scriptPath +" "+"-x"+" "+ executPath
    # print (cmd)
    retcode = subprocess.call(cmd, shell=True) 
    if retcode != 0: sys.exit(retcode)