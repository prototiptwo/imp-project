from pydantic import BaseModel, EmailStr
from typing import Optional


class ReaderBase(BaseModel):
    name: str
    email: EmailStr


class ReaderCreate(ReaderBase):
    pass


class ReaderUpdate(ReaderBase):
    pass


class ReaderInDB(ReaderBase):
    id: int

    class Config:
        from_attributes = True
