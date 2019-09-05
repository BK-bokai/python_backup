#coding=utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib


file1 = 'C:\\Users\\wm\\Desktop\\102.txt'



sender = 'bokai830124@simenvi.com.tw'
receivers = [ ]
receivers.append('bokai830124@gmail.com')



msg = MIMEMultipart()
msg['Subject']=subject    
msg['From']=sender      
msg['To']=receivers[0]       


part_text=MIMEText(email_text)
msg.attach(part_text)             



part_attach1 = MIMEApplication(open(file1,'rb').read())   
part_attach1.add_header('Content-Disposition','attachment',filename=file) 
msg.attach(part_attach1)   



smtp= smtplib.SMTP('localhost')  

smtp.sendmail(sender, receivers, msg.as_string())

print('郵件傳送成功！')