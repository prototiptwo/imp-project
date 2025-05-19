"""
Модуль управления выдачей и возвратом книг
Реализует:
- Выдачу книги читателю (с проверкой доступности)
- Возврат книги (с проверкой принадлежности)
- Получение списка активных займов
Все операции требуют аутентификации
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app.db.session import get_db
from app.schemas.transactions import BorrowRecord, BorrowCreate
from app.crud.transactions import (
    borrow_book as crud_borrow,
    return_book as crud_return,
    get_active_borrows,
    check_reader_borrow_limit,
    check_book_availability,
)
from app.api.deps import get_current_user
from app.crud.books import get_book
from app.crud.readers import get_reader

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post(
    "/borrow", response_model=BorrowRecord, dependencies=[Depends(get_current_user)]
)
def borrow_book(borrow: BorrowCreate, db: Session = Depends(get_db)):
    """Выдать книгу читателю"""
    # Проверка существования книги и читателя
    book = get_book(db, book_id=borrow.book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    reader = get_reader(db, reader_id=borrow.reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")

    # Проверка бизнес-логики
    if not check_book_availability(db, borrow.book_id):
        raise HTTPException(status_code=400, detail="Book not available")

    if check_reader_borrow_limit(db, borrow.reader_id):
        raise HTTPException(status_code=400, detail="Reader has too many books")

    # Создание записи о выдаче
    return crud_borrow(db=db, borrow=borrow)


@router.post("/return/{borrow_id}", dependencies=[Depends(get_current_user)])
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    """Вернуть книгу в библиотеку"""
    borrow_record = crud_return(db=db, borrow_id=borrow_id)
    if not borrow_record:
        raise HTTPException(
            status_code=404, detail="Borrow record not found or already returned"
        )
    return {"message": "Book returned successfully"}


@router.get(
    "/active/{reader_id}",
    response_model=List[BorrowRecord],
    dependencies=[Depends(get_current_user)],
)
def get_reader_active_borrows(reader_id: int, db: Session = Depends(get_db)):
    """Получить список активных займов читателя"""
    reader = get_reader(db, reader_id=reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return get_active_borrows(db, reader_id=reader_id)
