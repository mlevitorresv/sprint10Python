from models.model import Model
from config.sql import mydb
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
        print(cursor.rowcount, "record inserted.")
        
        return(f'the data was collected correctly \n {self.data}')

    def update(self):
        room_modify = self.view()
        print(f"Element to modify:\n{room_modify}")
        field = ''
        
        while field not in room_modify:
            field = input('Enter an existing field to modify\n')
        
        data = input(f'Enter data to {field}\n')
        room_modify[field] = data
        return(room_modify)