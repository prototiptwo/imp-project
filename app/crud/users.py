from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.users import UserCreate
from app.core.security import get_password_hash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
