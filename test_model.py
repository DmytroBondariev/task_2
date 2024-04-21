import pytest
from pydantic import ValidationError
from users.schemas import User


def test_user_model_validation():
    user_data = {
        "id": 1,
        "username": "testuser",
        "email": "testuser@gmail.com",
        "password": "testpassword",
        "sex": "Male"
    }
    user = User.model_validate(user_data)
    assert user.dict() == user_data


def test_user_model_enum_invalidation():
    user_data = {
        "id": 1,
        "username": "testuser",
        "email": "testuser@gmail.com",
        "password": "testpassword",
        "sex": "InvalidSex"
    }
    with pytest.raises(ValidationError):
        User.model_validate(user_data)
