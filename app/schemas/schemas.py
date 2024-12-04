import uuid

from pydantic import BaseModel, Field


class AuthorIn(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    date_of_birth: int | None = Field(default=None)


class AuthorOut(BaseModel):
    id: int
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    date_of_birth: int | None = Field(default=None)


class BookIn(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    genre: str | None = Field(default=None, max_length=50)
    publication_year: int | None = Field(default=None)
    author_id: int = Field(..., description="ID of the author this book is associated with")


class BookOut(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=100)
    genre: str | None = Field(default=None, max_length=50)
    publication_year: int | None = Field(default=None)
    author_id: int


class UserIn(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    date_of_birth: int | None = Field(default=None)
    email: str = Field(min_length=7, max_length=50)
    password: str = Field(min_length=8, max_length=50)
    confirm_password: str = Field(min_length=8, max_length=50)
    username: str = Field(min_length=7, max_length=50)


class UserOut(BaseModel):
    id: int
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    date_of_birth: int | None = Field(default=None)
    email: str = Field(min_length=7, max_length=50)
    password: str = Field(min_length=8, max_length=50)
    username: str = Field(min_length=7, max_length=50)