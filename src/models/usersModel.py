from models.model import Model

class UsersModel(Model):
    path = "src\\data\\users.json"
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

    def update(self):
        user_modify = self.view()
        print(f"Element to modify:\n{user_modify}")

        field = input('Enter field to modify\n')
        data = input(f'Enter data to {field}\n')

        user_modify[field] = data
        print(user_modify)








        