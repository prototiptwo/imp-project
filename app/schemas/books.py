from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str


class BookCreate(BookBase):
    year: Optional[int] = None
    isbn: Optional[str] = None
    copies_available: int = 1
    description: Optional[str] = None


class BookUpdate(BookCreate):
    pass


class BookInDB(BookBase):
    id: int
    year: Optional[int]
    isbn: Optional[str]
    copies_available: int
    description: Optional[str]

    class Config:
        from_attributes = True
