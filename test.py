import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = 'bokai830124@simenvi.com.tw'
receivers = [ ]
receivers.append('bokai830124@gmail.com')


for receiver in receivers:
    message = MIMEText('Python test', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] =  receiver

    subject = 'simenvi test'
    message['Subject'] = Header(subject, 'utf-8')



    try:
        smtpObj = smtplib.SMTP('localhost')

        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("yes")
    except smtplib.SMTPException:
        print ("Error")




