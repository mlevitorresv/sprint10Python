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
        with open(cls.path) as file:
            data = json.load(file)
            
            find_id = input('Enter id of element:\n')            
            for i in data:
                if i['id'] == int(find_id):
                    return(i)
    
    @classmethod
    def delete():
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def update():
        pass