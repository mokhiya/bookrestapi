from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from app.database import engine


class Authors(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    date_of_birth: int | None = Field(default=None)
    books: List["Books"] = Relationship(back_populates="author")


def create_tables():
    SQLModel.metadata.create_all(bind=engine)


class Books(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(min_length=3, max_length=100)
    genre: str | None = Field(default=None)
    publication_year: int | None = Field(default=None)

    author_id: int = Field(foreign_key="authors.id")
    author: Optional[Authors] = Relationship(back_populates="books")

def create_tables():
    SQLModel.metadata.create_all(bind=engine)