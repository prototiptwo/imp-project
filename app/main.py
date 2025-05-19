"""
Главный модуль приложения FastAPI
Объединяет все компоненты API и настраивает приложение
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.session import engine, Base
from app.api import auth, books, readers, transactions
from app.core.config import settings

async def test_db_connection():
    try:
        async with engine.connect() as conn:
            print("✅ Подключение к PostgreSQL успешно!")
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")

import logging

logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI

app = FastAPI(
    title="Library API",
    description="API для управления библиотекой",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Library API"}

# Создание таблиц БД (для разработки, в production используйте миграции)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

print(f"Current settings: {settings.model_dump()}")  # Проверить все настройки

def create_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="API для управления библиотечным каталогом",
        version="1.0.0",
    )

    # Настройка CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Подключение роутеров
    app.include_router(auth.router)
    app.include_router(books.router)
    app.include_router(readers.router)
    app.include_router(transactions.router)

    # События запуска/остановки
    @app.on_event("startup")
    async def startup_event():
        await create_tables()
        print("Application started")

    @app.on_event("shutdown")
    async def shutdown_event():
        print("Application shutdown")

    return app


app = create_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
