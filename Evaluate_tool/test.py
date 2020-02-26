import mysql.connector
import re, time
import xlsxwriter
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="bokai",    
  passwd="2841p4204",   
  database="tw_sim_evaluate"
)



# now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
# Time_period = '2019-06-01_2016-06-30'
start = '2019-06-01'
end   = '2019-06-02'
workdir = 'test'

# # mycursor = mydb.cursor()
# # sql = "INSERT INTO test (Time_Period, Create_at) VALUES (%s, %s)"
# # val = (Time_period, now)
# # mycursor.execute(sql, val)
 
# # mydb.commit()   
 
# # print(mycursor.rowcount, "记录插入成功。")

mycursor = mydb.cursor()

# sql = "UPDATE evaluate-tasks SET Path = '"+workdir+"' WHERE Time_Period = " +"'" +start+'_'+end + "'"
sql = "UPDATE evaluate-tasks SET Finish = 'test' WHERE Time_Period = '2019-06-01_2016-06-02'"

mycursor.execute(sql)
 0
mydb.commit()
 
# print(mycursor.rowcount, " 条记录被修改")

print(sql)
