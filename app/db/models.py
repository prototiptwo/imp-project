from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.session import engine, Base  
from .session import Base

class User(Base):
    """Модель пользователя (библиотекаря)"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Book(Base):
    """Модель книги"""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    year = Column(Integer)
    isbn = Column(String, unique=True)
    copies_available = Column(Integer, default=1, nullable=False)
    description = Column(String)


class Reader(Base):
    """Модель читателя"""

    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class BorrowedBook(Base):
    """Модель выданной книги"""

    __tablename__ = "borrowed_books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    borrow_date = Column(DateTime, default=func.now(), nullable=False)
    return_date = Column(DateTime)
    due_date = Column(DateTime)

    book = relationship("Book")
    reader = relationship("Reader")
# Тестовое задание для компании Патрес. Сделал Романов Лев Алексеевич
