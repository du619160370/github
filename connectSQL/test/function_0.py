import pymysql

def test_function(hw_name, time, hw_detail, rate_of_process):
    # connect with database
    conn  = pymysql.connect(host = '127.0.0.1', 
                           user = 'dubin',
                           passwd = '123asdASD!@#',
                           db = 'dubinDB',
                           port = 3306,
                           charset = 'utf8mb4')

    cursor = conn.cursor()
    
    # commond sentence
    sql = f'INSERT INTO homework_status(\
    hw_name, time, hw_detail, rate_of_process)\
    VALUES(\
    "{hw_name}", "{time}", "{hw_detail}", "{rate_of_process}");'
    
    cursor.execute(sql)
    conn.commit()
    cursor.close()

    cursor = conn.cursor()
    sql = 'SELECT * FROM homework_status;'
    raw_id = cursor.execute(sql) - 1
    cursor.scroll(raw_id, mode = 'absolute')
    content = cursor.fetchone()
    result = content[0] + ',' +  str(content[1]) + ',' + content[2] + ',' + content[3]
    # print(result)
    cursor.close()
    conn.close()
    
    return result






