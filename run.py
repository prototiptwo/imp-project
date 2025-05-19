import sys
from pathlib import Path
import uvicorn

# Добавляем корень проекта в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Теперь reload будет работать!
    )