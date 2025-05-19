from pydantic_settings import BaseSettings
from typing import ClassVar  # Добавьте этот импорт

class Settings(BaseSettings):
    PROJECT_NAME: str = "Library API"
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    SECRET_KEY: str = "secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

# Критически важная строка:
settings = Settings()