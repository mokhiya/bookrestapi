from fastapi import Depends, APIRouter, status, HTTPException

from app.cores.database import SessionDeb
from app.cores.models import Users
from app.cores.security.auth import get_password_hash, validate_password, get_user_by_username, get_user_by_email
from app.schemas.schemas import UserIn, UserOut

router = APIRouter(
    tags=['Authorization API'],
)


@router.post('/register/', status_code=status.HTTP_201_CREATED)
async def register(user_in: UserIn, session: SessionDeb) -> UserOut:
    if not validate_password(password=user_in.password, confirm_password=user_in.confirm_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect password.'
        )
    if get_user_by_username(username=user_in.username, session=session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username already registered.'
        )
    if get_user_by_email(email=user_in.email, session=session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already exists.'
        )
    user_dict = user_in.dict()
    user_dict.pop('confirm_password')
    user_dict["password"] = get_password_hash(user_in.password)

    user = Users(**user_dict)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user



@router.post('/login/')
async def login(username: str, password: str):
    pass


@router.post('/logout/')
async def logout():
    pass


@router.post('/verify/code/')
async def logout():
    pass


@router.post('/resend/code/')
async def logout():
    pass
