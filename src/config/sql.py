import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database='dashboardhotelmiranda',
    user = "root",
    password = "12345678"
)

print(mydb)