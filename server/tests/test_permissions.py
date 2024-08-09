from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_permissions():
    response = client.get("/permissions")
    assert response.status_code == 200


def test_post_permissions():
    response = client.post("/permissions")
    assert response.status_code == 200


def test_get_permission():
    response = client.get("/permissions/1")
    assert response.status_code == 200


def test_update_permission():
    response = client.put("/permissions/1")
    assert response.status_code == 200


def test_delete_permissions():
    response = client.delete("/permissions/1")
    assert response.status_code == 200
