#! python3
import pymysql

# 项目信息
project_name = '迭代76'

# 当前目录
current_dir = 'E:/autotest/TestReport/76/'

# 建立数据库连接
conn = pymysql.connect(
    host='192.168.0.88',
    port=8080,
    user='zentao',
    passwd='zentao',
    db='zentao',
    charset='utf8')

# 接收邮箱
email_address_list = ['test@gaiay.cn']