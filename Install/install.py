from setup import setting, table

db_build = setting.main()

if db_build == "clear":
    table_build = table.main()
    if table_build == "clear":
        print("ALL CLEAR")
    else:
        print("Table_Build ERROR")
else:
    print("DB_Build ERROR")