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
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all users: {results}")



    def update(self):
        cursor = mydb.cursor()
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
                
        fields_to_modify = []
        data_to_fields = []        
        
        user_modify = self.view()
        print(f"Element to modify:\n{user_modify}")
        choose = input(f'\n Choose field to modify (q for exit): {fields} \n')
        while choose != 'q':
            data = input(f'\nEnter data to {fields[choose]}\n')
            fields_to_modify.append(fields[choose])
            data_to_fields.append(data)
            choose = input(f'\n Choose other field to modify (q for exit): {fields} \n')
            
        set_clause = ','.join([f"{field} = %s" for field in fields_to_modify])
        mydb.reconnect()
        query = (f"UPDATE {self.table} SET {set_clause} WHERE id = %s")
        cursor.execute(query, data_to_fields + [user_modify[0]['id']])
        mydb.commit()
            
        return 'Update completed.'