from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from auth.oauth2 import oauth2_schema
from users.schemas import User, UserCreate
from users import crud
from dependencies import get_async_session

router = APIRouter()


@router.get("/users/", response_model=list[User])
async def get_all_users(db: AsyncSession = Depends(get_async_session), token: str = Depends(oauth2_schema)):
    """
    Retrieves a list of all users from the database.

    Args:
        db (AsyncSession): The database session to use for the query.

    Returns:
        list: A list of User instances representing the users.
        :param db:
        :param token:
    """
    return await crud.get_users_list(db_session=db)


@router.post("/users/", response_model=User)
async def create_user(
        user: UserCreate, db: AsyncSession = Depends(get_async_session)
):
    """
    Creates a new user in the database.

    Args:
        user (UserCreate): An instance of UserCreate representing the user to create.
        db (AsyncSession): The database session to use for the query.

    Returns:
        User: An instance of User representing the created user, or raises a 400 error if the user could not be created.
    """
    try:
        return await crud.create_user(db_session=db, user=user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with provided username or email already exists")


@router.get("/users/{user_id}/", response_model=User)
async def user_detail(user_id: int, db_session: AsyncSession = Depends(get_async_session)):
    """
    Retrieves the details of a specific user from the database.

    Args:
        user_id (int): The ID of the user to retrieve.
        db_session (AsyncSession): The database session to use for the query.

    Returns:
        User: An instance of User representing the user, or raises a 404 error if no user with the given ID was found.
    """
    db_user = await crud.get_user_detail(db_session=db_session, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user
