from models.model import Model

class BookingsModel(Model):
    path = "src\\data\\bookings.json"
    data = {
        'photo': 'http://dummyimage.com/150x100.png/dddddd/000000',
        'id': 0,
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
        
        while True:
            try:
                self.data['id'] = int(input('Enter id: '))
                break
            except ValueError:
                print('Error: Enter a valid id')  
              
        self.data['name'] = input('Enter name: ')
        self.data['orderDate'] = input('Enter orderDate: ')
        self.data['orderTime'] = input('Enter orderTime: ')
        self.data['checkInDate'] = input('Enter checkInDate: ')
        self.data['checkInTime'] = input('Enter checkInTime: ')
        self.data['checkOut'] = input('Enter checkOut: ')
        self.data['checkOutTime'] = input('Enter checkOutTime: ')
        self.data['notes'] = input('Enter notes: ')
        
        while True:
            try:
                self.data['room'] = int(input('Enter roomId: '))
                break
            except ValueError:
                print('Error: Enter a valid roomId')

        self.data['status'] = input('Enter status: ')
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

