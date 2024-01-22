from abc import ABC

class Model(ABC):
    
    @classmethod
    def list(cls):
        print(f"Listing from {cls.path}")

    pass