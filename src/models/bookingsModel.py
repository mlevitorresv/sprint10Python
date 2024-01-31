from models.model import Model
import datetime
from config.sql import mydb


class BookingsModel(Model):
    table = "bookings"
    data = {
        'photo': '',
        'name': '',
        'orderDate': '',
        'orderTime': '',
        'checkInDate': '',
        'checkInTime': '',
        'checkOut': '',
        'checkOutTime': '',
        'notes': '',
        'room': '',
        'status': ''
    }

    def create(self):
        self.data['photo'] = input('Enter photo: ')
        self.data['name'] = input('Enter name: ')
        self.data['orderDate'] = datetime.datetime.now().date()
        self.data['orderTime'] = datetime.datetime.now().time()
        self.data['checkInDate'] = input('Enter checkInDate (YYYY/MM/DD): ')
        checkindate = self.data['checkInDate'].split('/')
        checkincomplete = datetime.datetime(int(checkindate[0]), int(checkindate[1]), int(checkindate[2]), 12, 00)
        
        
        self.data['checkOut'] = input('Enter checkOutDate (YYYY/MM/DD): ')
        checkoutdate = self.data['checkOut'].split('/')
        checkoutcomplete = datetime.datetime(int(checkoutdate[0]), int(checkoutdate[1]), int(checkoutdate[2]), 12, 00)
        
        
        self.data['notes'] = input('Enter notes: ')
        
        while True:
            try:
                self.data['room'] = int(input('Enter roomId: '))
                break
            except ValueError:
                print('Error: Enter a valid roomId')

        
        while True:
            try:
                self.data['status'] = bool(input('Enter status: '))
                break
            except ValueError:
                print('Error: Enter a valid status value (True or False)')
                
        cursor = mydb.cursor()
        query = (f"INSERT INTO {self.table} (photo, name, orderDate, orderTime, checkinDate, checkinTime, checkout, checkoutTime, notes, roomId, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (self.data['photo'], self.data['name'], self.data['orderDate'], self.data['orderTime'], checkincomplete.date(), checkincomplete.time(), checkoutcomplete.date(), checkoutcomplete.time(), self.data['notes'], self.data['room'], self.data['status'])
        cursor.execute(query, values)
        mydb.commit()
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all bookings: {results}")



    def update(self):
        cursor = mydb.cursor()
        fields = {
            '1': 'photo',
            '2': 'name',
            '3': 'checkInDate',
            '4': 'checkOut',
            '5': 'notes',
            '6': 'room',
            '7': 'status',
            'q': 'quit'
        }
                
        booking_modify = self.view()
        print(f"Element to modify:\n{booking_modify}")
        choose = input(f'\n Choose field to modify (q for exit): {fields} \n')
        
        while choose != 'q':
            data = input(f'\nEnter data to {fields[choose]}\n')
            mydb.reconnect()
            query = (f"UPDATE {self.table} SET {fields[choose]} = %s WHERE id = %s")
            cursor.execute(query, (data, booking_modify[0]['id']))
            mydb.commit()
            choose = input(f'\n Choose other field to modify (q for exit): {fields} \n')
            
        return 'Update completed.'
        

