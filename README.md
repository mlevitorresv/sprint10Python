<h1>Hotel Management</h1><br/>
A Python program for managing a hotel, allowing the creation of users, rooms, reservations, and the management of user feedback about the hotel. The program is designed to be operated through the command-line interface, utilizing argparse actions for all the aforementioned functionalities.

<h3>📓How to Use 💻</h3>

<ol>
    <li>Clone this project with: git clone https://github.com/mlevitorresv/sprint10Python.git</li>
    <li>Create a virtual environment with: python -m venv env</li>
    <li>Activate the virtual environment with: source /env/bin/activate</li>
    <li>Install requirements with: pip install -r requirements.txt</li>
    <li>Get it running! Execute: python src/app.py [action]</li>
</ol>

```python
actions = {
    'read-users': 'show all users',
    'read-rooms': 'show all rooms',
    'read-bookings': 'show all bookings',
    'read-contacts': 'show all contacts',
    'read-user-id': 'show one user',
    'read-room-id': 'show one room',
    'read-booking-id': 'show one booking',
    'read-contact-id': 'show one contact',
    'create-user': 'create a user',
    'create-room': 'create a room',
    'create-booking': 'create a booking',
    'create-contact': 'create a contact',
    'update-user': 'update a user',
    'update-room': 'update a room',
    'update-booking': 'update a booking',
    'update-contact': 'update a contact',
    'delete-user': 'delete a user',
    'delete-room': 'delete a room',
    'delete-booking': 'delete a booking',
    'delete-contact': 'delete a contact',
    }
```
