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
        self.data['id'] = int(input('Enter id: '))
        self.data['name'] = input('Enter name: ')
        self.data['orderDate'] = input('Enter orderDate: ')
        self.data['orderTime'] = input('Enter orderTime: ')
        self.data['checkInDate'] = input('Enter checkInDate: ')
        self.data['checkInTime'] = input('Enter checkInTime: ')
        self.data['checkOut'] = input('Enter checkOut: ')
        self.data['checkOutTime'] = input('Enter checkOutTime: ')
        self.data['notes'] = input('Enter notes: ')
        self.data['room'] = input('Enter room: ')
        self.data['status'] = input('Enter status: ')
        print(f'the data was collected correctly \n {self.data}')

    def update(self):
        booking_modify = self.view()
        print(f"Element to modify:\n{booking_modify}")

        field = input('Enter field to modify\n')
        data = input(f'Enter data to {field}\n')

        booking_modify[field] = data
        print(booking_modify)

