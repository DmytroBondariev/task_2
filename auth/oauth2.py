from datetime import datetime, timedelta
from secrets import token_urlsafe
from typing import Optional

import jwt
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/task_2/login")

SECRET_KEY = token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(payload: dict, expires_delta: Optional[timedelta] = None):
    to_encode = payload.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# def get_current_user(token: str = Depends(oauth2_schema), db: AsyncSession = Depends(get_async_session)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#
#     try:
#         payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
#         decode_email = payload.get("user_email")
#
#         if decode_email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#
#     user = get_user_by_email(db_session=db, email=decode_email)
#
#     if user is None:
#         raise credentials_exception
#
#     return user
