from abc import ABC, abstractmethod
import json

class Model(ABC):
    
    @classmethod
    def list(cls):
        print(f"Listing from {cls.path}")
        f = open(cls.path)
        data = json.load(f)
        print(data)

    @classmethod
    def view(cls):
        print(f"Listing from {cls.path}")
        f = open(cls.path)
        data = json.load(f)

        print('Enter id of element')
        find_id = input()
        
        for i in data:
            if i['id'] == int(find_id):
                print(i)
    
    @classmethod
    def delete():
        pass

    # @abstractmethod
    # def create():
    #     pass

    # @abstractmethod
    # def update():
    #     pass