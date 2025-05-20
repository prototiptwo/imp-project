# Library Management API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

RESTful API для управления библиотечным каталогом с JWT-аутентификацией.

## 📌 Функционал

- **Аутентификация** (JWT)
  - Регистрация библиотекарей
  - Вход с получением токена
- **Управление книгами**
  - CRUD-операции
  - Поиск и фильтрация
- **Управление читателями**
  - Добавление/редактирование
- **Выдача книг**
  - Контроль лимитов (не более 3 книг)
  - Возврат книг

## 🛠 Технологии

- Python 3.8+
- FastAPI
- SQLAlchemy (async)
- PostgreSQL/SQLite
- JWT-аутентификация
- Alembic (миграции)
- Pydantic (валидация)

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
git clone https://github.com/prototiptwo/imp-project.git
cd imp-project