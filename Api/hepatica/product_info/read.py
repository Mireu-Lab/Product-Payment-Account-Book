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

def product_info(product_name):
    sql = f"SELECT * FROM product_info_DB WHERE product_name={product_name};"

    cursor.execute(sql)
    result = cursor.fetchall()

    read.close()
    return result