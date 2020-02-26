import glob
import os
import subprocess, sys
import os

filePath = 'D:\\bokai\\python\\python-code\\calmet\\20191216案例\\模擬結果\\plot.BAS'

files = os.listdir("D:\\bokai\\python\\python-code\\calmet\\20191216案例\\模擬結果\\uv") 
for x in files:
    time=x.replace("uv.txt","")
    Year=time[0:4]
    Month=time[4:6]
    Day=time[6:8]
    Hr=time[9:11]
    Minute=time[11:13]

    outfilepath='D:\\bokai\\python\\python-code\\calmet\\20191216案例\\模擬結果\\plotscript\\'+time+'_plot'+'.BAS'
    
    fp3=open(filePath,"r")
    fp4=open(outfilepath,"w")
 
    for s in fp3.readlines():#先读出来
        step1= s.replace("年",Year) 
        step2= step1.replace("月",Month)
        step3= step2.replace("日",Day)
        step4= step3.replace("時",Hr)
        step5= step4.replace("分",Minute)
        fp4.write(step5)

    fp3.close()
    fp4.close()

    scriptPath = '"C:\Program Files\Golden Software\Surfer 13\Scripter\Scripter.exe"'
    executPath = '"D:\/bokai\python\python-code\calmet\/20191216案例\模擬結果\/plotscript\/'+time+'_plot'+'.BAS'+'"'

    cmd=scriptPath +" "+"-x"+" "+ executPath
    # # print (cmd)
    retcode = subprocess.call(cmd, shell=True) 
    if retcode != 0: sys.exit(retcode)