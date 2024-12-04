from urllib import request

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.cores.database import SessionDeb
from app.cores.models import Authors
from app.schemas.schemas import AuthorIn

router = APIRouter(
    tags=['Authors'],
)


@router.post("/authors/", status_code=201)
async def create_author(author: AuthorIn, session: SessionDeb):
    author_in = AuthorIn(**author.dic())
    session.add(author_in)
    session.commit()
    session.refresh(author_in)
    return author_in


@router.get("/authors/", status_code=200)
async def get_author(session: SessionDeb):
    authors = session.exec(select(Authors)).all()
    return authors


@router.delete("/authors/{author_id}", status_code=204)
async def delete_author(author_id: int, session: SessionDeb):
    authors = session.exec(select(Authors)).where(Authors.id == author_id).first()
    if not authors:
        raise HTTPException(status_code=404, detail="Author not found")

    session.delete(authors)
    session.commit()
    return {'status': True, 'detail': 'Deleted successfully'}


@router.put("/authors/{author_id}", status_code=200)
async def update_author(author_id: int, session: SessionDeb):
    author = session.execute(select(Authors).where(Authors.id == author_id)).scalar_one_or_none()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    data = await request.json()

    for key, value in data.items():
        if hasattr(author, key):
            setattr(author, key, value)

    session.commit()
    session.refresh(author)

    return {"status": True, "detail": "Updated successfully", "data": {
        "id": author.id,
        "first_name": author.first_name,
        "last_name": author.last_name,
        "email": author.email
    }}