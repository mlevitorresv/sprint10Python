from abc import ABC, abstractmethod
import json

class Model(ABC):
    
    @classmethod
    def list(cls):
        with open(cls.path) as file:
            return(file.read())

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