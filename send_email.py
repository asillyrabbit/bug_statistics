#!Python

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import configuration

# 邮件通知函数
def send_email(filenames=[],email_address_list=[]):

    # 接收邮箱
    receives = email_address_list
    filenames = filenames

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Tester",'utf-8')
    #message['To'] = Header("Tester",'utf-8')
    subject = '每日自动统计测试日报'
    message['Subject'] = Header(subject,'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('测试日报见附件...','plain','utf-8'))


    # 构造附件
    for filename in filenames:
        att = MIMEText(open(configuration.current_dir + filename ,'rb').read(),'base64','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] =  'attachment; filename=' + filename
        message.attach(att)

   
    # 连接到SMTP服务器
    smtpObj = smtplib.SMTP('smtp.ym.163.com', 25)
    smtpObj.ehlo()
    smtpObj.starttls()

    # 登录发送邮箱
    smtpObj.login('test@gaiay.cn', 'password')

    # 发送
    smtpObj.sendmail('test@gaiay.cn', receives, message.as_string())

    # 从SMTP服务器断开
    smtpObj.quit()