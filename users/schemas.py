from pydantic import BaseModel
from users.models import SexEnum


class UserBase(BaseModel):
    """
    A Pydantic model representing the base attributes of a user. This model includes fields for the user's username,
    email, password, and sex.

    Args:
        username (str): The user's username.
        email (str): The user's email.
        password (str): The user's password.
        sex (SexEnum): The user's sex. Must be one of the values defined in the SexEnum class.
    """
    username: str
    email: str
    password: str
    sex: SexEnum


class UserCreate(UserBase):
    """
    A Pydantic model representing the data required to create a new user. This model inherits all fields from UserBase,
    so it includes fields for the user's username, email, password, and sex.
    """
    pass


class User(UserBase):
    """
    A Pydantic model representing a user. This model inherits all fields from UserBase and adds an 'id' field.

    Args:
        id (int): The user's ID.
    """
    id: int

    class ConfigDict:
        """
        A nested class for Pydantic model configuration. The 'from_attributes' attribute is set to True, which means
        that attributes of the model instance will be used to populate the dictionary when the model is converted to a
        dictionary using the 'dict()' function.
        """
        from_attributes = True
