import argparse
from models.usersModel import UsersModel;
from models.roomsModel import RoomsModel;
from models.bookingsModel import BookingsModel;
from models.contactsModel import ContactsModel;


parser  = argparse.ArgumentParser(description='options to management elements')
parser.add_argument('action')
args = parser.parse_args()

action = args.action

def read_rooms():
    print(RoomsModel.list())
def read_room():
    print(RoomsModel.view())
def create_room():
    print(RoomsModel.create())
def update_room():
    print(RoomsModel.update())
def delete_room():
    print(RoomsModel.delete())

def read_users():
    print(UsersModel.list())
def read_user():
    print(UsersModel.view())
def create_user():
    print(UsersModel.create())
def update_user():
    print(UsersModel.update())
def delete_user():
    print(UsersModel.delete())

def read_contacts():
    print(ContactsModel.list())
def read_contact():
    print(ContactsModel.view())
def create_contact():
    print(ContactsModel.create())
def update_contact():
    print(ContactsModel.update())
def delete_contact():
    print(ContactsModel.delete())

def read_bookings():
    print(BookingsModel.list())
def read_booking():
    print(BookingsModel.view())
def create_booking():
    print(BookingsModel.create())
def update_booking():
    print(BookingsModel.update())
def delete_booking():
    print(BookingsModel.delete())


my_actions = {
    'read-users': read_users,
    'read-rooms': read_rooms,
    'read-bookings': read_bookings,
    'read-contacts': read_contacts,
    'read-user-id': read_user,
    'read-room-id': read_room,
    'read-booking-id': read_booking,
    'read-contact-id': read_contact,
    'create-user': create_user,
    'create-room': create_room,
    'create-booking': create_booking,
    'create-contact': create_contact,
    'update-user': update_user,
    'update-room': update_room,
    'update-booking': update_booking,
    'update-contact': update_contact,
    'delete-user': delete_user,
    'delete-room': delete_room,
    'delete-booking': delete_booking,
    'delete-contact': delete_contact,
    }

if action in my_actions:
    my_actions[action]()
else:
    print(f'action not recognized {action}')