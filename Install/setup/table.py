import pymysql
import json

with open("Data/info.json", "r+", encoding='UTF-8') as info:
    password = json.load(info)

setup_db = pymysql.connect(
    user='hepatica_user', 
    passwd='hepatica0427', 
    host=password["sql_server_host"],
    port=password["sql_server_port"],
    db='hepatica', 
    charset='utf8'
)

cursor = setup_db.cursor(pymysql.cursors.DictCursor)

sql1 = """
create table staff_account_DB (
  id int unsigned not null auto_increment primary key,
  staff_name text not null,
  phone text not null,
  email text not null,
  work_times_start int null,
  work_times_end int null,
  password varchar(255) null
);
"""
sql2 = """
create table staff_work_status_DB (
  id int unsigned not null auto_increment primary key,
  staff_name text not null,
  work_result BOOLEAN null,
  attendance_status text null
);
"""
sql3 = """
create table product_info_DB (
  id int unsigned not null auto_increment primary key,
  product_name text null,
  info_url text null
);
"""
sql4 = """
create table account_book_DB (
  id int unsigned not null auto_increment primary key,
  product text null,
  staff text null,
  payment BOOLEAN null
);
"""

sql_line = [sql1, sql2, sql3, sql4]

def main():
    for i in sql_line:
        try:
            cursor.execute(i)
            setup_table.commit()
        except:
            pass        
    cursor.close()
    
    return "clear"