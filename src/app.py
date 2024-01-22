import argparse
from models.usersModel import UsersModel;
from models.roomsModel import RoomsModel;


parser = parser = argparse.ArgumentParser(description='options to management elements')
parser.add_argument('action')
args = parser.parse_args()

action = args.action


if action == 'read-users':
    User = UsersModel()
    User.list()
elif action == 'read-rooms':
    Room = RoomsModel()
    Room.list()
elif action == 'read-bookings':
    Room = RoomsModel()
    Room.list()
elif action == 'read-contacts':
    Room = RoomsModel()
    Room.list()