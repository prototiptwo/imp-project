from sqlalchemy.orm import Session
from app.db.models import Book
from app.schemas.books import BookCreate, BookUpdate


def get_book(db: Session, book_id: int = None, isbn: str = None):
    query = db.query(Book)
    if book_id:
        query = query.filter(Book.id == book_id)
    if isbn:
        query = query.filter(Book.isbn == isbn)
    return query.first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, db_book: Book, book: BookUpdate):
    for field, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db.query(Book).filter(Book.id == book_id).delete()
    db.commit()
