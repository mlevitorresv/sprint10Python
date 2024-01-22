from abc import ABC

class Model(ABC):
    
    @classmethod
    def list(path):
        print(f"Listing from {path}")

    pass