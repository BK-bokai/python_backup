from datetime import datetime

now=datetime.now()
# print(now)
# print('年:',now.year, '月:',now.month,'日:' ,now.day)
# print(datetime(2015,1,1,12))
delta=datetime(2015,1,1) - datetime(2014,8,10)
print(delta)

# #String to Datetime
# A='2016-07-07 14:30:22'
# date=datetime.strptime(A,'%Y-%m-%d %H:%M:%S')
# print(date)

# date=datetime(2015,1,1)

# str_date= datetime.strftime(date,'%Y-%m-%d %H:%M:%S')
# print(str_date)

A="01-22_02"
date=datetime.strptime(A,'%m-%d_%H')
print(date.month, date.day)


print(datetime.now())
print(datetime.now() + datetime.timedelta(days=1))
# print(datetime.now() + datetime.timedelta(hours=1))
# print(datetime.now() + datetime.timedelta(minutes=1))
# print(datetime.now() + datetime.timedelta(seconds=1))
