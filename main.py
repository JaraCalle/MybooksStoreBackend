from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from models import Book
import crud

app = FastAPI(title="Books API")


app = FastAPI(title="Books API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"msg": "API running healthy"}

@app.get("/api")
def api():
    return {"msg": "My book store"}

@app.get("/api/books")
def read_books():
    return crud.get_all_books()

@app.get("/api/books/{book_id}")
def read_book(book_id: str):
    book = crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/api/books")
def add_book(book: Book):
    return crud.create_book(book)
