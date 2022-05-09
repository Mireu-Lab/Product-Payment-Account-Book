import pymysql

read = pymysql.connect(
    user='root', 
    passwd='mireu041214', 
    host='192.168.0.2',
    port=3305,
    db='hepatica',
    charset='utf8'
)

cursor = read.cursor(pymysql.cursors.DictCursor)

sql = f"SELECT * FROM staff_account_DB;"

cursor.execute(sql)
result = cursor.fetchall()

read.close()
print(result)