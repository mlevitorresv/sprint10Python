from models.model import Model

class RoomsModel(Model):
    path = "src\\data\\rooms.json"
    data = {
        'photo': '',
        'id': 0,
        'type': '',
        'bed': '',
        'amenities': '',
        'description': '',
        'rate': 0,
        'price': 0,
        'discount': 0,
        'available': False
    }

    def create(self):
        self.data['photo'] = input('Enter photo: ')
        self.data['id'] = int(input('Enter id: '))
        self.data['type'] = input('Enter type: ')
        self.data['bed'] = input('Enter bed: ')
        self.data['amenities'] = input('Enter amenities: ')
        self.data['rate'] = int(input('Enter rate: '))
        self.data['price'] = int(input('Enter price: '))
        self.data['discount'] = int(input('Enter discount: '))
        self.data['available'] = input('Enter available: ')
        print(f'the data was collected correctly \n {self.data}')

    def update(self):
        room_modify = self.view()
        print(f"Element to modify:\n{room_modify}")

        field = input('Enter field to modify\n')
        data = input(f'Enter data to {field}\n')

        room_modify[field] = data
        print(room_modify)