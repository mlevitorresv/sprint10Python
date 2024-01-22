from abc import ABC
import json

class Model(ABC):
    
    @classmethod
    def list(cls):
        print(f"Listing from {cls.path}")
        f = open(cls.path)
        data = json.load(f)
        print(data)