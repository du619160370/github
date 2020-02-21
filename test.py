import pymssql

server = "187.32.43.13"
user = "123"
password = "123"

conn = pymssql.conect(server, user, password, "连接默认数据库名称�")
