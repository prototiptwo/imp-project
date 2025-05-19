"""
Модуль управления книгами
Реализует CRUD операции для книг:
- Создание (только для аутентифицированных пользователей)
- Получение списка (публичное)
- Получение деталей книги
- Обновление
- Удаление
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.books import BookCreate, BookUpdate, BookInDB
from app.crud.books import get_book, get_books, create_book, update_book, delete_book
from app.api.deps import get_current_user

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[BookInDB])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить список всех книг (публичный доступ)"""
    books = get_books(db, skip=skip, limit=limit)
    return books


@router.post("/", response_model=BookInDB, dependencies=[Depends(get_current_user)])
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу (требуется аутентификация)"""
    db_book = get_book(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="ISBN already exists")
    return create_book(db=db, book=book)


@router.get("/{book_id}", response_model=BookInDB)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Получить информацию о конкретной книге"""
    db_book = get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put(
    "/{book_id}", response_model=BookInDB, dependencies=[Depends(get_current_user)]
)
def update_existing_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """Обновить информацию о книге (требуется аутентификация)"""
    db_book = get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return update_book(db=db, db_book=db_book, book=book)


@router.delete("/{book_id}", dependencies=[Depends(get_current_user)])
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу (требуется аутентификация)"""
    db_book = get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    delete_book(db=db, book_id=book_id)
    return {"ok": True}
