from models.model import Model

class ContactsModel(Model):
    table = "comment"
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
        
        while True:
            try:
                self.data['id'] = int(input('Enter id: '))
                break
            except ValueError:
                print('Error: Enter a valid id')
        self.data['name'] = input('Enter name: ')
        self.data['date'] = input('Enter date: ')
        self.data['email'] = input('Enter email: ')
        
        while True:
            try:
                self.data['phone'] = int(input('Enter phone: '))
                break
            except ValueError:
                print('Error: Enter a valid phone')        
        self.data['description'] = input('Enter description: ')
        self.data['status'] = input('Enter status: ')
        return(f'the data was collected correctly \n {self.data}')

    def update(self):
        contact_modify = self.view()
        print(f"Element to modify:\n{contact_modify}")
        field = ''
        
        while field not in contact_modify:
            field = input('Enter an existing field to modify\n')
            
        data = input(f'Enter data to {field}\n')

        contact_modify[field] = data
        return(contact_modify)