import argparse
from models.usersModel import UsersModel;
from models.roomsModel import RoomsModel;
from models.bookingsModel import BookingsModel;
from models.contactsModel import ContactsModel;


parser  = argparse.ArgumentParser(description='options to management elements')
parser.add_argument('action')
args = parser.parse_args()

action = args.action

my_actions = {
    'read-users': UsersModel().list,
    'read-rooms': RoomsModel().list,
    'read-bookings': BookingsModel().list,
    'read-contacts': ContactsModel().list,
    'read-user-id': UsersModel().view,
    'read-room-id': RoomsModel().view,
    'read-booking-id': BookingsModel().view,
    'read-contact-id': ContactsModel().view,
    'create-user': UsersModel().create,
    'create-room': RoomsModel().create,
    'create-booking': BookingsModel().create,
    'create-contact': ContactsModel().create,
    'update-user': UsersModel().update,
    'update-room': RoomsModel().update,
    'update-booking': BookingsModel().update,
    'update-contact': ContactsModel().update,
    'delete-user': UsersModel().delete,
    'delete-room': RoomsModel().delete,
    'delete-booking': BookingsModel().delete,
    'delete-contact': ContactsModel().delete,
    }

if action in my_actions:
    my_actions[action]()
else:
    print(f'action not recognized {action}')