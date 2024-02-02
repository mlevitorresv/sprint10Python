from config.sql import mydb

sql_path = 'src\\data\\dashboardhotelmiranda.sql'

try:
    cursor = mydb.cursor()

    with open(sql_path) as sql:
        sql_script = sql.read()
    
    sql_commands = sql_script.split(';')

    for command in sql_commands:
        if command.strip():  # Ignorar líneas en blanco
            cursor.execute(command)
    mydb.commit()
except Exception as e:
    print(f'Error: {e}')
finally:
    if cursor:
        cursor.close()