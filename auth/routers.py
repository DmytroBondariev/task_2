from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from auth.oauth2 import create_access_token
from dependencies import get_async_session
from auth.hash_password import verify_password
from users.crud import get_user_by_username

router = APIRouter(tags=["authentication"])


@router.post("/login")
async def get_token(request: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    user = await get_user_by_username(db_session=session, username=request.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(plain_password=request.password, hashed_password=user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = create_access_token(payload={"username": user.username})

    return {"access_token": access_token, "token_type": "bearer", "user": user.username, "email": user.email}

# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
