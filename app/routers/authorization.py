from fastapi import Depends, APIRouter, status

from app.cores.database import SessionDeb
from app.cores.models import Users
from app.schemas.schemas import UserIn, UserOut

router = APIRouter(
    tags=['Authorization API'],
)


@router.post('/register/', status_code=status.HTTP_201_CREATED)
async def register(user_in: UserIn, session: SessionDeb) -> UserOut:
    user = Users(**user_in.dict())
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
