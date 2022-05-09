import pymysql
import json

with open("Data/info.json", "r+", encoding='UTF-8') as info:
    password = json.load(info)

write = pymysql.connect(
    user='hepatica_user', 
    passwd='hepatica0427', 
    host=password["sql_server_host"],
    port=password["sql_server_port"],
    db='hepatica', 
    charset='utf8'
)
cursor = write.cursor(pymysql.cursors.DictCursor)

def info(staff_name, phone, email, work_times_start, work_times_end, password):
    sql = f"INSERT INTO account_book_DB (staff_name, phone, email, work_times_start, work_times_end, password) VALUES ('{staff_name}', '{phone}', '{email}', {work_times_start}, {work_times_end}, '{password}');"
    cursor.execute(sql)
    write.commit()
    cursor.close()
    
def update(staff_name, phone, email, work_times_start, work_times_end, password):
    sql = f"UPDATE account_book_DB SET staff_name='{staff_name}', phone='{phone}', email='{email}', work_times_start={work_times_start}, work_times_end={work_times_end};"
    cursor.execute(sql)
    write.commit()
    cursor.close()
    
def remove(staff_name):
    sql = f"""DELETE FROM account_book_DB WHERE staff_name='{staff_name}';"""
    cursor.execute(sql)
    write.commit()
    cursor.close()
    