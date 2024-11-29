from fastapi import FastAPI

from app.models import create_tables
from app.routers import authors, books

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_tables()
@app.get("/")
async def root():
    return {"message": "Welcome to my library data!"}


app.include_router(authors.router)
app.include_router(books.router)