from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Books, Authors
from app.database import get_session
from app.schemas import BookIn, BookOut

router = APIRouter(
    tags=['Books'],
)


@router.post("/books/", status_code=201, response_model=BookOut)
async def create_book(book: BookIn, session: Session = Depends(get_session)):
    # Validate if the author exists
    author = session.execute(select(Authors).where(Authors.id == book.author_id)).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_book = Books(**book.dict())
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@router.get("/books/", status_code=200, response_model=list[BookOut])
async def get_books(session: Session = Depends(get_session)):
    books = session.execute(select(Books)).scalars().all()
    return books


@router.get("/books/{book_id}", status_code=200, response_model=BookOut)
async def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.execute(select(Books).where(Books.id == book_id)).scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# Update a book
@router.put("/books/{book_id}", status_code=200, response_model=BookOut)
async def update_book(book_id: int, request: Request, session: Session = Depends(get_session)):
    book = session.execute(select(Books).where(Books.id == book_id)).scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    data = await request.json()
    for key, value in data.items():
        if hasattr(book, key):
            setattr(book, key, value)

    session.commit()
    session.refresh(book)
    return book


@router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.execute(select(Books).where(Books.id == book_id)).scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()
    return {"status": True, "detail": "Deleted successfully"}
