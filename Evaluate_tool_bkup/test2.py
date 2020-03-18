import MySQLdb
import time




#connect() 方法用於建立資料庫的連線，裡面可以指定引數：使用者名稱，密碼，主機等資訊。
#這只是連線到了資料庫，要想操作資料庫需要建立遊標。
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='bokai',
        passwd='2841p4204',
        db ='tw_sim_evaluate',
        )


#通過獲取到的資料庫連線conn下的cursor()方法來建立遊標。
cur = conn.cursor()

#插入一條資料
# cur.execute("insert into test values('test2','2016-06-02_2016-06-03','test2')")
# now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

# SQL="INSERT INTO test(Time_Period,Finish,Create_at) VALUES('2016-06-02_2016-06-03','False','%s')" % now     #新增紀錄
# cur.execute(SQL)   

# conn.commit()                     #操作結果寫入資料庫

#修改查詢條件的資料
cur.execute("update evaluate_tasks set Path='test',Finish='%d' where Time_Period = '2016-06-01_2016-06-02'" % True)
conn.commit() 

#刪除查詢條件的資料
# cur.execute("delete from test where Time_Period = '2016-06-02_2016-06-03'")
# conn.commit()
# print(SQL)