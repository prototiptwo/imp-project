import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.append(str(Path(__file__).parent))

try:
    from app.main import app

    print("Импорт успешен!")
except Exception as e:
    print(f"Ошибка: {e}")
    print("sys.path:", sys.path)
