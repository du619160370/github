import csv
import pymysql

def conn_host(host1, user1, passwd1, db1, port1, charset1):
    '''连接sql数据库，host1数据库地址，user1用户名，passwd1密码，db1数据库名称，port1端口，chartset1编码格式'''
    global conn
    conn = pymysql.connect(host = host1,
                           user = user1,
                           passwd = passwd1,
                           db = db1,
                           port = port1,
                           charset = charset1)

def load_sql(tablename, data_column, data_list):
    '''tablename表名,data_column字段列表,data_list数据列表'''
    cursor = conn.cursor()
    sql = 'INSERT INTO ' + tablename + '('
    for i in data_column:
        sql = sql + i + ','
    sql = sql[:-1]
    sql = sql + ') VALUES (' + '%s,' * len(data_column)
    sql = sql[:-1] + ');'
    # sql = 'INSERT INTO (xxx,xxx,..) VALUES (%s,%s,...);'
    # print(sql)
    # 由于单句插入数据很耗费时间，采用所短时间的批量插入
    cursor.executemany(sql, data_list)
    conn.commit()
    cursor.close()

def load_file(fileaddress, tablename):
    '''fileaddress读入文件绝对路径，tablename需要输入数据的表名'''
    with open(fileaddress, 'r') as f:
        # print('Open file successful.')
        f_csv = csv.reader(f)
        headers = next(f_csv)   # 字段名列表
        data_list = []
        for i in f_csv:
            data_list.append(i)
            if len(data_list) > 200000:   # 由于一次批量插入会造成内存使用过量，所以限制每次插入的大小
                load_sql(tablename, headers, data_list)
                data_list.clear()
        load_sql(tablename, headers, data_list)
        data_list.clear()


    



# main

fileaddress = '/home/dubin/Downloads/UserBehavior.csv'
host = '127.0.0.1'
user = 'dubin'
passwd = '123asdASD!@#'
db = 'dubinDB'
port = 3306
charset = 'utf8mb4'
tablename = 'User'

conn_host(host, user, passwd, db, port, charset)
# print('Connect successful.')
print('插入中...')
load_file(fileaddress, tablename)
conn.close()
print('插入完成.')



