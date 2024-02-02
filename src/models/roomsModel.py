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
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all rooms: {results}")
        

    def update(self):
        cursor = mydb.cursor()
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
        
        fields_to_modify = []
        data_to_fields = []
                
        room_modify = self.view()
        print(f"Element to modify:\n{room_modify}")
        choose = input(f'\n Choose field to modify (q for exit): {fields} \n')
        while choose != 'q':
            data = input(f'\nEnter data to {fields[choose]}\n')
            fields_to_modify.append(fields[choose])
            data_to_fields.append(data)
            choose = input(f'\n Choose other field to modify (q for exit): {fields} \n')

        set_clause = ','.join([f"{field} = %s" for field in fields_to_modify])
        mydb.reconnect()
        query = (f"UPDATE {self.table} SET {set_clause} WHERE id = %s")
        cursor.execute(query, data_to_fields + [room_modify[0]['id']])
        mydb.commit()
            
        return 'Update completed.'
