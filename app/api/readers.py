"""
Модуль управления читателями
Реализует CRUD операции для читателей:
- Создание
- Получение списка
- Получение деталей
- Обновление
- Удаление
Все операции требуют аутентификации
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.readers import ReaderCreate, ReaderUpdate, ReaderInDB
from app.crud.readers import (
    get_reader,
    get_readers,
    create_reader,
    update_reader,
    delete_reader,
)
from app.api.deps import get_current_user

router = APIRouter(prefix="/readers", tags=["readers"])


@router.post("/", response_model=ReaderInDB, dependencies=[Depends(get_current_user)])
def create_new_reader(reader: ReaderCreate, db: Session = Depends(get_db)):
    """Создать нового читателя"""
    db_reader = get_reader(db, email=reader.email)
    if db_reader:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_reader(db=db, reader=reader)


@router.get(
    "/", response_model=List[ReaderInDB], dependencies=[Depends(get_current_user)]
)
def read_readers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить список всех читателей"""
    return get_readers(db, skip=skip, limit=limit)


@router.get(
    "/{reader_id}", response_model=ReaderInDB, dependencies=[Depends(get_current_user)]
)
def read_reader(reader_id: int, db: Session = Depends(get_db)):
    """Получить информацию о читателе"""
    db_reader = get_reader(db, reader_id=reader_id)
    if db_reader is None:
        raise HTTPException(status_code=404, detail="Reader not found")
    return db_reader


@router.put(
    "/{reader_id}", response_model=ReaderInDB, dependencies=[Depends(get_current_user)]
)
def update_reader_info(
    reader_id: int, reader: ReaderUpdate, db: Session = Depends(get_db)
):
    """Обновить информацию о читателе"""
    db_reader = get_reader(db, reader_id=reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return update_reader(db=db, db_reader=db_reader, reader=reader)


@router.delete("/{reader_id}", dependencies=[Depends(get_current_user)])
def delete_reader_record(reader_id: int, db: Session = Depends(get_db)):
    """Удалить читателя"""
    db_reader = get_reader(db, reader_id=reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    delete_reader(db=db, reader_id=reader_id)
    return {"ok": True}
