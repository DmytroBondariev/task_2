from sqlalchemy import Column, Integer, String, Enum
from enum import StrEnum

from database import Base

class SexEnum(StrEnum):
    """
    Enumeration for the sex of a user. This enumeration is used in the UserDB model to restrict the possible values
    of the 'sex' field to 'Male' and 'Female'.
    """
    MALE = "Male"
    FEMALE = "Female"


class UserDB(Base):
    """
    SQLAlchemy model representing a user in the database. This model includes fields for the user's ID, username,
    email, sex, and password.

    The 'id' field is an integer that serves as the primary key. The 'username' and 'email' fields are strings that
    must be unique. The 'sex' field is an enumeration that must be one of the values defined in the SexEnum class.
    The 'password' field is a string.

    Args:
        id (Integer): The user's ID. Serves as the primary key.
        username (String): The user's username. Must be unique.
        email (String): The user's email. Must be unique.
        sex (Enum): The user's sex. Must be one of the values defined in the SexEnum class.
        password (String): The user's password.
    """
    __tablename__ = "users_DTO"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    sex = Column(Enum(SexEnum), nullable=False)
    password = Column(String)
