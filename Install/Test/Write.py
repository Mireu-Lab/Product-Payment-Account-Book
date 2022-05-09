import pymysql

write = pymysql.connect(
    user='root', 
    passwd='mireu041214', 
    host='192.168.0.2',
    port=3305,
    db='hepatica',
    charset='utf8'
)

cursor = write.cursor(pymysql.cursors.DictCursor)

def info(staff_name, phone, email, work_times_start, work_times_end, password):
    sql = f"INSERT INTO staff_account_DB (staff_name, phone, email, work_times_start, work_times_end, password) VALUES ('{staff_name}', '{phone}', '{email}', {work_times_start}, {work_times_end}, '{password}');"
    cursor.execute(sql)
    write.commit()
    cursor.close()
    
def update(staff_name, phone, email, work_times_start, work_times_end, password):
    sql = f"UPDATE staff_account_DB SET staff_name='{staff_name}', phone='{phone}', email='{email}', work_times_start={work_times_start}, work_times_end={work_times_end};"
    cursor.execute(sql)
    write.commit()
    cursor.close()
    
def remove(staff_name):
    sql = f"""DELETE FROM staff_account_DB WHERE staff_name='{staff_name}';"""
    cursor.execute(sql)
    write.commit()
    cursor.close()
    