from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid
app = FastAPI()

class Book(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str = None
    author: str = None
    year: int = 0
    genre: str = None

books = []

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return HTTPException(status_code=200)


@app.get("/books")
def list_books() -> list[Book]:
    return books

@app.get("/books/{book_id}")
def get_book(book_id: uuid.UUID) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    return HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def get_book(book_id: uuid.UUID):
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
            return HTTPException(status_code=200)

    return HTTPException(status_code=404, detail="Book not found")


'''

    id: int = None (integer, auto - increment or UUID)


Create a small RESTful API for a simple Book Library system using FastAPI. The API should allow users to:
Add a book
List all books
Get a single book by ID
Delete a book by ID

Book Model:
Each book should have the following fields:
id (integer, auto-increment or UUID)
title (string)
author (string)
year (integer)
genre (optional, string)

'''