from models.model import Model

class ContactsModel(Model):
    path = "src\\data\\comment.json"
    data = {
        'photo': '',
        'id': 0,
        'name': '',
        'date': '',
        'email': '',
        'phone': '',
        'description': '',
        'status': ''
    }

    def create(self):
        self.data['photo'] = input('Enter photo: ')
        self.data['id'] = int(input('Enter id: '))
        self.data['name'] = input('Enter name: ')
        self.data['date'] = input('Enter date: ')
        self.data['email'] = input('Enter email: ')
        self.data['phone'] = input('Enter phone: ')
        self.data['description'] = input('Enter description: ')
        self.data['status'] = input('Enter status: ')
        print(f'the data was collected correctly \n {self.data}')