'''对connect_mysql.py进行修改，添加对于数据库的增、删、改功能，添加一次可进行多个操作'''
import pymysql

def insert_into():
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
    print('-' * 100)

def select_all():
    cursor = conn.cursor()
    sql = 'SELECT * FROM homework_status;'
    cursor.execute(sql)
    table_data = cursor.fetchall()
    print('\n作业名称 /  时间 /  作业详情 /  完成进度')
    print()
    for i in table_data:
        a = ''
        for j in i:
            a = a + f'  {j}  /'
        print(a[2:-2])
        print()
    cursor.close()
    print('-' * 100)

def delete_data():
    cursor = conn.cursor()
    id_del = input('请输入需要删除的"作业名称": ')
    sql = f'DELETE FROM homework_status WHERE hw_name = "{id_del}";'
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    print('-' * 100)

def update_data():
    cursor = conn.cursor()
    name = input('请输入需要修改信息的"作业名称": ')
    item = input('请输入需要修改的项目(作业名称/时间/作业详情/完成进度): ')
    contant = input('请输入需要修改的为的内容(时间格式 年-月-日 时-分-秒): ')
    items_dic = {'作业名称': 'hw_name', '时间': 'time', '作业详情': 'hw_detail', '完成进度': 'rate_of_process'}
    item = items_dic[item]
    sql = f'UPDATE homework_status SET {item} = "{contant}" WHERE hw_name = "{name}";'
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    print('-' * 100)


# main
# connect with database
conn  = pymysql.connect(host = '127.0.0.1', 
                       user = 'dubin',
                       passwd = '123asdASD!@#',
                       db = 'dubinDB',
                       port = 3306,
                       charset = 'utf8mb4')

while True:
    user = input('请输入指令(插入数据/查看数据/删除数据/修改数据/退出): ')
    if user == '插入数据':
        insert_into()
    elif user == '查看数据':
        select_all()
    elif user == '删除数据':
        delete_data()
    elif user == '修改数据':
        update_data()
    elif user == '退出':
        break
    else:
        print('输入错误')

conn.close()

