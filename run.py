#!Python

import statistics
import os
import charts
import send_email
import send2trash
import combine
import configuration

os.chdir(configuration.current_dir)

# 接收邮箱
email_address_list = configuration.email_address_list

# 统计并生成报告
statistics

# 合并报告(当生成了多个报告时，合并成一个)
combine

# 生成图表
for filename in os.listdir():
    if filename.startswith('XXX-' + configuration.project_name):
       charts.generate_charts(filename)


# 发送邮件
filenames = []
for filename in os.listdir():
    if filename.startswith('XXX-' + configuration.project_name):
        filenames.append(filename)

send_email.send_email(filenames,email_address_list)

# 删除本地文件
for filename in os.listdir():
    if filename.endswith('-测试日报.xlsx'):
        send2trash.send2trash(filename)