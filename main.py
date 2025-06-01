from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid

app = FastAPI()

class Book(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    author: str
    year: int
    genre: str = None

books = []

# GET: /
@app.get("/")
def root():
    return {"message": "Book Library API"}

# POST: /books
@app.post("/books", status_code=201)
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully", "book": book}

# GET: /books
@app.get("/books")
def list_books() -> list[Book]:
    return books

# GET: /books/{book_id}
@app.get("/books/{book_id}")
def get_book(book_id: uuid.UUID) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: /books/{book_id}
@app.delete("/books/{book_id}")
def get_book(book_id: uuid.UUID):
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
            return HTTPException(status_code=200)
    raise HTTPException(status_code=404, detail="Book not found")


'''
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