import argparse
from models.usersModel import UsersModel;
from models.roomsModel import RoomsModel;


parser = parser = argparse.ArgumentParser(description='options to management elements')
parser.add_argument('action')
args = parser.parse_args()

action = args.action


if action == 'user':
    User = UsersModel()
    User.list()
elif action == 'room':
    Room = RoomsModel()
    Room.list()
