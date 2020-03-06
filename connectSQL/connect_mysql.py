'''在SQL数据库dubinDB中，表homework_status中写入作业名称，时间，作业详情，完成进度，时间自动取当时时间'''
import pymysql

# connect with database
conn  = pymysql.connect(host = '127.0.0.1', 
                       user = 'dubin',
                       passwd = '123asdASD!@#',
                       db = 'dubinDB',
                       port = 3306,
                       charset = 'utf8mb4')


# create cursor and get information
cursor = conn.cursor()
hw_name = input("作业名称：")
hw_detail = input("作业详情：")
rate_of_process = input("完成进度：")

# commond sentence
sql = f'INSERT INTO homework_status(\
hw_name, time, hw_detail, rate_of_process)\
VALUES(\
"{hw_name}", NOW(), "{hw_detail}", "{rate_of_process}");'

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
print('完成')

