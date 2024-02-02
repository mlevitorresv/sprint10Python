from models.model import Model
from config.sql import mydb
from utils import update_element
import json

class RoomsModel(Model):
    table = "rooms"
    data = {
        'number': 0,
        'photo': '',
        'type': '',
        'bed': '',
        'amenities': [],
        'description': '',
        'rate': 0,
        'price': 0,
        'discount': 0,
        'available': False
    }

    def create(self):
        while True:
            try:
                self.data['number'] = float(input('Enter number: '))
                break
            except ValueError:
                print('Error: Enter a valid number')
                
        self.data['photo'] = input('Enter photo: ')
        self.data['type'] = input('Enter type: ')
        self.data['bed'] = input('Enter bed: ')
        
        while True:
            amenity = input('Enter one amenity (Enter for nothing): ')
            
            if not amenity:
                break;
        
            self.data['amenities'].append(amenity)
            
        amenities = json.dumps(self.data['amenities'])
            
        self.data['description'] = input('Enter description: ')
        
        while True:
            try:
                self.data['rate'] = float(input('Enter rate: '))
                break
            except ValueError:
                print('Error: Enter a valid rate')

        while True:
            try:
                self.data['price'] = float(input('Enter price: '))
                break
            except ValueError:
                print('Error: Enter a valid price')

        while True:
            try:
                self.data['discount'] = int(input('Enter discount: '))
                break
            except ValueError:
                print('Error: Enter a valid discount')  
                      
        while True:
            try:
                self.data['available'] = bool(input('Enter available: '))
                break
            except ValueError:
                print('Error: Enter a valid available value (True or False)')
        
        cursor = mydb.cursor()
        query = (f"INSERT INTO {self.table} (number, photo, type, bed, amenities, description, rate, price, discount, available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (self.data['number'], self.data['photo'], self.data['type'], self.data['bed'], amenities, self.data['description'], self.data['rate'], self.data['price'], self.data['discount'], self.data['available'])
        cursor.execute(query, values)
        mydb.commit()
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all rooms: {results}")
        

    def update(self):
        fields = {
            '1': 'number',
            '2': 'photo',
            '3': 'type',
            '4': 'bed',
            '5': 'amenities',
            '6': 'description',
            '7': 'rate',
            '8': 'price',
            '9': 'discount',
            '10': 'available',
            'q': 'quit'
        }
        print(update_element(fields, self))
