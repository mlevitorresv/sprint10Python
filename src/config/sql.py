import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
    host = db_host,
    database = db_database,
    user = db_user,
    password = db_password
)

print(mydb)