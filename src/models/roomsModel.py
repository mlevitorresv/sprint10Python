from models.model import Model

class RoomsModel(Model):
    table = "rooms"
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
        
        while True:
            try:
                self.data['id'] = int(input('Enter id: '))
                break
            except ValueError:
                print('Error: Enter a valid id')
                
        self.data['type'] = input('Enter type: ')
        self.data['bed'] = input('Enter bed: ')
        self.data['amenities'] = input('Enter amenities: ')
        
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
                      
        self.data['available'] = input('Enter available: ')
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