import pytest
from models.roomsModel import RoomsModel
from models.usersModel import UsersModel
from models.bookingsModel import BookingsModel
from models.contactsModel import ContactsModel


def test_list_rooms():
    assert isinstance(RoomsModel.list(), list)

def test_list_users():
    assert isinstance(UsersModel.list(), list)

def test_list_bookings():
    assert isinstance(BookingsModel.list(), list)

def test_list_contacts():
    assert isinstance(ContactsModel.list(), list)