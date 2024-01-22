import argparse
from models.usersModel import UsersModel;
from models.roomsModel import RoomsModel;
from models.bookingsModel import BookingsModel;
from models.contactsModel import ContactsModel;


parser  = argparse.ArgumentParser(description='options to management elements')
parser.add_argument('action')
args = parser.parse_args()

action = args.action


if action == 'read-users':
    UsersModel.list()
elif action == 'read-rooms':
    RoomsModel.list()
elif action == 'read-bookings':
    BookingsModel.list()
elif action == 'read-contacts':
    ContactsModel.list()