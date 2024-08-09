from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_post_users():
    response = client.post("/users")
    assert response.status_code == 200


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200


def test_update_user():
    response = client.put("/users/1")
    assert response.status_code == 200


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
