"""
Пакет приложения библиотечного API

Инициализирует основные компоненты и делает доступными ключевые объекты
"""

from fastapi import FastAPI
from app.db.session import engine, Base
from .core.config import settings

# Делаем важные компоненты доступными при импорте из app
__all__ = ["create_app", "engine", "Base", "settings"]


def create_app():
    """Фабрика для создания экземпляра приложения"""
    app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")
    return app
