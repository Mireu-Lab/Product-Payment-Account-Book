import pymysql
import json

with open("Data/info.json", "r+", encoding='UTF-8') as info:
    password = json.load(info)

read = pymysql.connect(
    user='hepatica_user', 
    passwd='hepatica0427', 
    host=password["sql_server_host"],
    port=password["sql_server_port"],
    db='hepatica', 
    charset='utf8'
)
cursor = read.cursor(pymysql.cursors.DictCursor)

def account_book():
    sql = f"SELECT * FROM account_book_DB;"

    cursor.execute(sql)
    result = cursor.fetchall()

    read.close()
    return result