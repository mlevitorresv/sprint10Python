import pytest
from ..models.roomsModel import RoomsModel


def test_get_room_id(monkeypatch):
    id_input_mock = 3

    monkeypatch.setattr('builtins.input', lambda _: id_input_mock)

    assert(RoomsModel.view())