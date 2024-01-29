from abc import ABC, abstractmethod
from config.sql import mydb
import mysql.connector

class Model(ABC):
    
    @classmethod
    def list(cls):
        cursor = mydb.cursor()
        query = (f"SELECT * FROM {cls.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        mydb.close()
        
        return results

    @classmethod
    def view(cls):
        find_id = input('Enter id of element:\n')    
        cursor = mydb.cursor()
        query = (f"SELECT * FROM {cls.table} WHERE id = {find_id}")
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        mydb.close()
        
        return data
        
    @classmethod
    def delete():
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def update():
        pass