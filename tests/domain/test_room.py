import uuid
import json
from rentomatic.domain.room import Room


def test_room_model_init():
    code = uuid.uuid4()
    room = Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    room = Room.model_validate(init_dict)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_to_dict():
    init_dict = {
        "code": uuid.uuid4(),
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    room = Room.model_validate(init_dict)
    assert room.model_dump() == init_dict


def test_room_model_comparison():
    init_dict = {
        "code": uuid.uuid4(),
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    room1 = Room.model_validate(init_dict)
    room2 = Room.model_validate(init_dict)
    assert room1 == room2


def test_room_serialization_to_json():
    code = uuid.uuid4()
    room = {
        "code": code,
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    expected_json = f"""
        {{
        "code": "{code}",
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293
        }}
    """
    room = Room.model_validate(room)
    json_room = room.model_dump_json()
    assert json.loads(expected_json) == json.loads(json_room)
