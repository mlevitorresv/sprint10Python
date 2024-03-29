from models.model import Model
from config.sql import mydb
from utils import update_element
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
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all users: {results}")



    def update(self):
        fields = {
            '1': 'photo',
            '2': 'name',
            '3': 'date',
            '4': 'email',
            '5': 'phone',
            '6': 'description',
            '7': 'status',
            'q': 'quit'
        }
        print(update_element(fields, self))

        