# conding:utf-8


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, time, datetime
from email.header import Header

class MailUtils():
    @classmethod
    def send_test_report(cls):
        # 邮件配置信息
        sender = "lisy_program@163.com"
        receiver = "lisy_from@163.com"
        subject = "自动化测试报告"
        smtpserver = "smtp.163.com"
        auth_code = "aaa111"

        # 读取测试报告
        f = open('./report.html', 'rb')
        mail_body = f.read()
        f.close()

        # 编辑正文
        html = MIMEText(mail_body, _subtype="html", _charset="utf-8")
        html["Subject"] = subject
        html["from"] = sender
        html["to"] = receiver

        # 编辑附件
        att = MIMEText(mail_body, 'base64', 'gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="xdTestreport.html"'


        # 整合正文与附件
        msg = MIMEMultipart()
        msg['Subject'] = "测试报告主题"
        msg.attach(html) # 添加正文
        msg.attach(att) # 添加附件

        smtp = smtplib.SMTP()
        # 连接服务器
        smtp.connect("smtp.163.com")
        # 使用授权码登录
        smtp.login(sender, auth_code)
        # 发送邮件
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
