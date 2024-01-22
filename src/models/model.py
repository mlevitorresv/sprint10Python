from abc import ABC

class Model(ABC):
    
    @classmethod
    def list(cls):
        print(cls)

    pass