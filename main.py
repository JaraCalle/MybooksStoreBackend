from fastapi import FastAPI, HTTPException
from models import Book
import crud

app = FastAPI(title="Books API")

@app.get("/books")
def read_books():
    return crud.get_all_books()

@app.get("/books/{book_id}")
def read_book(book_id: str):
    book = crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books")
def add_book(book: Book):
    return crud.create_book(book)
