import pymysql
import json

with open("Data/info.json", "r+", encoding='UTF-8') as info:
    password = json.load(info)

setup_db = pymysql.connect(
    user="root", 
    passwd=password["root_password"], 
    host=password["sql_server_host"],
    port=password["sql_server_port"],
    charset='utf8'
)

cursor = setup_db.cursor(pymysql.cursors.DictCursor)

sql = "CREATE DATABASE hepatica;"
sql1 = "CREATE USER 'hepatica_user'@'%' IDENTIFIED BY 'hepatica0427';"
sql2 = "GRANT ALL PRIVILEGES ON hepatica.* TO 'hepatica_user'@'%';"

sql_line = [sql, sql1, sql2]

def main():
    for i in sql_line:
        try:
            cursor.execute(i)
            setup_db.commit()
        except:
            pass

    cursor.close()
    return "clear"