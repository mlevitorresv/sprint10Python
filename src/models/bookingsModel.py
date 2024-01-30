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
        print(cursor.rowcount, "record inserted.")
        
                
        return(f'the data was collected correctly \n {self.data}')



    def update(self):
        booking_modify = self.view()
        print(f"Element to modify:\n{booking_modify}")
        field = ''
        
        while field not in booking_modify:
            field = input('Enter an existing field to modify\n')
            
        data = input(f'Enter data to {field}\n')

        booking_modify[field] = data
        return(booking_modify)

