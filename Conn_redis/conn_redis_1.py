"""python3连接redis，实现String、Hash、Set、List 4种类型的基本操作
前提条件：redis服务已开启，host:127.0.0.1, port:6379, password:dubin"""
import redis

# String操作
def connect_redis(host1, passwd1, port1, db1):
    global r
    try:
        # host主机ip,password密码,db数据库,port端口
        # decode_responses默认输出字节字符串
        pool = redis.ConnectionPool(host = host1,
                                    password = passwd1,
                                    port = port1,
                                    db = db1,
                                    decode_responses = True)
        print("Connected success.")
    except:
        print("Could not connect to redis.")

    r = redis.Redis(connection_pool=pool)

def string_insert():
    content = input("请输入需要插入的键值：").split(' ')
    for i in range(0, len(content), 2):
        r.set(content[i], content[i+1])
    content.clear()

def string_get():
    keys = input("请输入需要查看值的键：").split(' ')
    for i in range(0, len(keys)):
        print(f"{keys[i]}: {r.get(keys[i])}")

# Hash操作
def hash_insert():
    h_name = input("请输入字典名称：")
    h_k_v = input("请输入需要插入字典的键值：").split(' ')
    h_dic = {}
    for i in range(0, len(h_k_v), 2):
        h_dic[h_k_v[i]] = h_k_v[i+1]
    r.hmset(h_name, h_dic)
    h_k_v.clear()
    h_dic.clear()

def hash_hgetall():
    h_name = input("请输入查询哈希字典名称：")
    h_dic = r.hgetall(h_name)
    for i in h_dic:
        print(f"{i}: {h_dic[i]}")
    h_dic.clear()

# List操作
def left_list_insert():
    list_name = input("请输入列表名：")
    content = input("请输入插入列表的值：").split(' ')
    for i in content:
        r.lpush(list_name, i)
    content.clear()

def right_list_insert():
    list_name = input("请输入列表名：")
    content = input("请输入插入列表的值：").split(' ')
    for i in content:
        r.rpush(list_name, i)
    content.clear()

def get_list():
    list_name = input("请输入查看的列表名：")
    print(r.lrange(list_name, '0', str(r.llen(list_name)-1)))

# Set操作
def set_insert():
    set_name = input("请输入集合名：")
    content = input("请输入插入集合的值：").split(' ')
    for i in content:
        r.sadd(set_name, i)
    content.clear()

def get_set():
    set_name = input("请输入要查看的集合名：")
    print(r.smembers(set_name))

def del_keys():
    keys_name = input("请输入需要删除的键的名称：").split(' ')
    for i in keys_name:
        r.delete(i)


host = '127.0.0.1'
passwd = 'dubin'
port = 6379
db = 0  # 0~15

connect_redis(host, passwd, port, db)

while True:
    print("\n1.字符串操作 2.列表操作 3.哈希操作 4.集合操作 5.删除内容")
    print("Ps: 输入quit退出。")
    flag1 = input("\n请输入操作指令：")
    if flag1 == '1':
        flag2 = input("1.插入键值对 2.查看键值对：")
        if flag2 == '1':
            string_insert()
        elif flag2 == '2':
            string_get()
    elif flag1 == '2':
        flag2 = input("1.列表左插入值 2.列表右插入值 3.查询列表内容：")
        if flag2 == '1':
            left_list_insert()
        elif flag2 == '2':
            right_list_insert()
        elif flag2 == '3':
            get_list()
    elif flag1 == '3':
        flag2 = input("1.插入哈希序列 2.查看哈希序列：")
        if flag2 == '1':
            hash_insert()
        elif flag2 == '2':
            hash_hgetall()
    elif flag1 == '4':
        flag2 = input("1.插入集合 2.查看集合内容：")
        if flag2 == '1':
            set_insert()
        elif flag2 == '2':
            get_set()
    elif flag1 == '5':
        del_keys()
    elif flag1 == 'quit':
        break
    





