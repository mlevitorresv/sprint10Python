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