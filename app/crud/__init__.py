"""
Пакет crud - операции с базой данных (Create, Read, Update, Delete)
"""
from .books import get_book, get_books, create_book, update_book, delete_book
from .readers import get_reader, get_readers, create_reader, update_reader, delete_reader
from .transactions import borrow_book, return_book, get_active_borrows

__all__ = [
    # Books
    'get_book', 'get_books', 'create_book', 'update_book', 'delete_book',
    # Readers
    'get_reader', 'get_readers', 'create_reader', 'update_reader', 'delete_reader',
    # Transactions
    'borrow_book', 'return_book', 'get_active_borrows'
]