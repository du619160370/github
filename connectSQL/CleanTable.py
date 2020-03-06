'''用于清空homework_status表格'''
import pymysql

# connect with database
conn  = pymysql.connect(host = '127.0.0.1', 
                       user = 'dubin',
                       passwd = '123asdASD!@#',
                       db = 'dubinDB',
                       port = 3306,
                       charset = 'utf8mb4')


cursor = conn.cursor()

# commond sentence
sql = f'TRUNCATE homework_status'

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
print('清理完成')

