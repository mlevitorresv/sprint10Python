from models.model import Model
from config.sql import mydb
import datetime



class ContactsModel(Model):
    table = "contacts"
    data = {
        'photo': '',
        'name': '',
        'email': '',
        'phone': '',
        'comment': '',
        'date': '',
        'dateTime': '',
        'archived': ''
    }

    def create(self):
        self.data['photo'] = input('Enter photo: ')
        self.data['name'] = input('Enter name: ')
        self.data['email'] = input('Enter email: ')
        
        while True:
            try:
                self.data['phone'] = int(input('Enter phone: '))
                break
            except ValueError:
                print('Error: Enter a valid phone')        
                
        self.data['comment'] = input('Enter comment: ')
        
        dateComplete = datetime.datetime.now()
        
        self.data['date'] = dateComplete.date()
        self.data['dateTime'] = dateComplete.time()
        
        
        while True:
            try:
                self.data['archived'] = bool(input('Enter archived: '))
                break
            except ValueError:
                print('Error: Enter a valid archived value (True or False)')
        
        cursor = mydb.cursor()
        query = (f"INSERT INTO {self.table} (photo, name, email, phone, comment, date, dateTime, archived) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        values = (self.data['photo'], self.data['name'], self.data['email'], self.data['phone'], self.data['comment'], self.data['date'], self.data['dateTime'], self.data['archived'])
        cursor.execute(query, values)
        mydb.commit()
        
        query = (f"SELECT * FROM {self.table}")
        cursor.execute(query)
        results = cursor.fetchall()
        

        
        return(f" all comments: {results}")

    def update(self):
        cursor = mydb.cursor()
        fields = {
            '1': 'photo',
            '2': 'name',
            '3': 'email',
            '4': 'phone',
            '5': 'comment',
            '6': 'archived',
            'q': 'quit'
        }
        
        fields_to_modify = []
        data_to_fields = []
                        
        contact_modify = self.view()
        print(f"Element to modify:\n{contact_modify}")
        choose = input(f'\n Choose field to modify (q for exit): {fields} \n')
        
        while choose != 'q':
            data = input(f'\nEnter data to {fields[choose]}\n')
            fields_to_modify.append(fields[choose])
            data_to_fields.append(data)
            choose = input(f'\n Choose other field to modify (q for exit): {fields} \n')

        set_clause = ','.join([f"{field} = %s" for field in fields_to_modify])
        mydb.reconnect()
        query = (f"UPDATE {self.table} SET {set_clause} WHERE id = %s")
        cursor.execute(query, data_to_fields + [contact_modify[0]['id']])
        mydb.commit()
            
        return 'Update completed.'