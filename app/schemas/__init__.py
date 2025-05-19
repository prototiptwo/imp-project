"""
Пакет schemas - Pydantic-схемы для валидации данных
"""
from .books import BookCreate, BookUpdate, BookInDB
from .readers import ReaderCreate, ReaderUpdate, ReaderInDB
from .transactions import BorrowCreate, BorrowRecord

__all__ = [
    'BookCreate', 'BookUpdate', 'BookInDB',
    'ReaderCreate', 'ReaderUpdate', 'ReaderInDB',
    'BorrowCreate', 'BorrowRecord'
]