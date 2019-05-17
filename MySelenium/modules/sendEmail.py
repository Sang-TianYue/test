# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import baseInfo
#from email.header import Header

def send_mail(testReport):
    f = open(testReport, 'rb')
    mail_body = f.read()
    f.close()

    try:
        smtp = smtplib.SMTP()
        smtp.connect(baseInfo.mail_server)
        sender = baseInfo.mail_send
        password = baseInfo.mail_password
        # 给多人发送邮件
        receiver = baseInfo.mail_receiver

        # 生成包含多个对象
        msg = MIMEMultipart()

        # 文本对象
        text = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = '自动化测试报告'
        msg['from'] = sender
        msg['To'] = ','.join(receiver)

        # 附件对象，参数分别为邮附件内容、text格式，编码格式
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file["Content-Type"] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename="report.html"'


        msg.attach(text)
        msg.attach(msg_file)

        smtp.login(sender, password)
        smtp.sendmail(sender, msg['To'].split(','), msg.as_string())
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False

