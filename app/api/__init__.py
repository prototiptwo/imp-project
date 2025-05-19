from .auth import router as auth_router
from .books import router as books_router
from .readers import router as readers_router
from .transactions import router as transactions_router

__all__ = ['auth_router', 'books_router', 'readers_router', 'transactions_router']