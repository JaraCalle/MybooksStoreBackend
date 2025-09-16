from database import books_table
from models import Book

def get_all_books():
    response = books_table.scan()
    return response.get("Items", [])

def get_book(book_id: str):
    response = books_table.get_item(Key={"id": book_id})
    return response.get("Item", None)

def create_book(book: Book):
    books_table.put_item(Item=book.dict())
    return book
