from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import UserDB, SexEnum
from users.schemas import UserCreate

from auth.hash_password import hash_password


async def get_users_list(
        db_session: AsyncSession,
        sex: SexEnum | None = None
):
    """
    Retrieves a list of users from the database. If a sex is provided, the function
    will return only users of that sex.

    Args:
        db_session (AsyncSession): The database session to use for the query.
        sex (SexEnum, optional): The sex of the users to retrieve. If None, users of all sexes are retrieved.

    Returns:
        list: A list of UserDB instances representing the users.
    """
    query = select(UserDB)

    if sex is not None:
        query = query.where(UserDB.sex == sex)

    user_list = await db_session.execute(query)

    return user_list.scalars().all()


async def create_user(db_session: AsyncSession, user: UserCreate):
    """
    Creates a new user in the database.

    Args:
        db_session (AsyncSession): The database session to use for the query.
        user (UserCreate): An instance of UserCreate representing the user to create.

    Returns:
        dict: A dictionary representing the created user.
    """
    hashed_password = hash_password(user.password)
    query = insert(UserDB).values(
        username=user.username,
        email=user.email,
        sex=user.sex.value,
        password=hashed_password
    )

    result = await db_session.execute(query)
    await db_session.commit()
    response = {**user.model_dump(), "id": result.lastrowid}
    return response


async def get_user_detail(db_session: AsyncSession, user_id: int):
    """
    Retrieves the details of a specific user from the database.

    Args:
        db_session (AsyncSession): The database session to use for the query.
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserDB: An instance of UserDB representing the user, or None if no user with the given ID was found.
    """
    query = select(UserDB).where(UserDB.id == user_id)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_username(db_session: AsyncSession, username: str):

    """
    Retrieves a user by their username.

    Args:
        db_session (AsyncSession): The database session to use for the query.
        username (str): The username of the user to retrieve.

    Returns:
        UserDB: An instance of UserDB representing the user, or None if no user with the given username was found.
    """
    query = select(UserDB).where(UserDB.username == username)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()
