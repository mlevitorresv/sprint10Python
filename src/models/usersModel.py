from models.model import Model
from config.sql import mydb
import datetime

class UsersModel(Model):
    table = "users"
    data = {
        'photo': '',
        'name': '',
        'date': '',
        'email': '',
        'phone': '',
        'description': '',
        'status': ''
    }

    def create(self):
        self.data['photo'] = input('Enter photo: ')   
        self.data['name'] = input('Enter name: ')
        self.data['date'] = input('Enter date (YYYY/MM/DD): ')
        self.data['email'] = input('Enter email: ')
        
        while True:
            try:
                self.data['phone'] = int(input('Enter phone: '))
                break
            except ValueError:
                print('Error: Enter a valid phone')
                
        self.data['description'] = input('Enter description: ')
        self.data['status'] = input('Enter status: ')
        
        dateElements =  self.data['date'].split('/')
        date = datetime.datetime(int(dateElements[0]), int(dateElements[1]), int(dateElements[2]))
        
        cursor = mydb.cursor()
        query = (f"INSERT INTO {self.table} (photo, name, date, email, phone, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        values = (self.data['photo'], self.data['name'], date.date(), self.data['email'], self.data['phone'], self.data['description'], self.data['status'])
        cursor.execute(query, values)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

        
        return(f'the data was collected correctly \n {self.data}')



    def update(self):
        user_modify = self.view()
        print(f"Element to modify:\n{user_modify}")
        field = ''
        
        while field not in user_modify:
            field = input('Enter an existing field to modify\n')
        
        data = input(f'Enter data to {field}\n')
        user_modify[field] = data
        return(user_modify)








        