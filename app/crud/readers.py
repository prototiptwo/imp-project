from sqlalchemy.orm import Session
from app.db.models import Reader
from app.schemas.readers import ReaderCreate, ReaderUpdate


def get_reader(db: Session, reader_id: int = None, email: str = None):
    query = db.query(Reader)
    if reader_id:
        query = query.filter(Reader.id == reader_id)
    if email:
        query = query.filter(Reader.email == email)
    return query.first()


def get_readers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reader).offset(skip).limit(limit).all()


def create_reader(db: Session, reader: ReaderCreate):
    db_reader = Reader(**reader.model_dump())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader


def update_reader(db: Session, db_reader: Reader, reader: ReaderUpdate):
    for field, value in reader.model_dump(exclude_unset=True).items():
        setattr(db_reader, field, value)
    db.commit()
    db.refresh(db_reader)
    return db_reader


def delete_reader(db: Session, reader_id: int):
    db.query(Reader).filter(Reader.id == reader_id).delete()
    db.commit()
