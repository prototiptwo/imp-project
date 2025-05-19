from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_access_protected_route_without_token():
    """Доступ без токена должен возвращать 401"""
    response = client.get("/api/books/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


def test_access_with_valid_token():
    """Доступ с валидным токеном должен работать"""
    # 1. Получаем токен
    auth_response = client.post(
        "/auth/login", json={"email": "admin@library.com", "password": "secret"}
    )
    token = auth_response.json()["access_token"]

    # 2. Делаем запрос с токеном
    response = client.get("/api/books/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
