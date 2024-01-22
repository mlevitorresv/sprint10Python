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
    'read-contacts': ContactsModel().list
    }

if action in my_actions:
    my_actions[action]()
else:
    print(f'action no recognized {action}')