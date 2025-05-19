from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db.models import BorrowedBook, Book
from app.schemas.transactions import BorrowCreate


def borrow_book(db: Session, borrow: BorrowCreate):
    # Уменьшаем количество доступных книг
    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if book.copies_available <= 0:
        raise ValueError("No copies available")
    book.copies_available -= 1

    # Создаем запись о выдаче
    db_borrow = BorrowedBook(
        book_id=borrow.book_id,
        reader_id=borrow.reader_id,
        due_date=datetime.now() + timedelta(days=30),
    )
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow


def return_book(db: Session, borrow_id: int):
    borrow = (
        db.query(BorrowedBook)
        .filter(BorrowedBook.id == borrow_id, BorrowedBook.return_date == None)
        .first()
    )

    if not borrow:
        return None

    # Увеличиваем количество доступных книг
    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    book.copies_available += 1

    # Отмечаем возврат
    borrow.return_date = datetime.now()
    db.commit()
    db.refresh(borrow)
    return borrow


def get_active_borrows(db: Session, reader_id: int):
    return (
        db.query(BorrowedBook)
        .filter(BorrowedBook.reader_id == reader_id, BorrowedBook.return_date == None)
        .all()
    )


def check_reader_borrow_limit(db: Session, reader_id: int, max_books: int = 3):
    active_borrows = (
        db.query(BorrowedBook)
        .filter(BorrowedBook.reader_id == reader_id, BorrowedBook.return_date == None)
        .count()
    )
    return active_borrows >= max_books


def check_book_availability(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book and book.copies_available > 0
