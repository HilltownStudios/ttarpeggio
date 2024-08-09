from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_roles():
    response = client.get("/roles")
    assert response.status_code == 200


def test_post_roles():
    response = client.post("/roles")
    assert response.status_code == 200


def test_get_record():
    response = client.get("/roles/1")
    assert response.status_code == 200


def test_update_record():
    response = client.put("/roles/1")
    assert response.status_code == 200


def test_delete_roles():
    response = client.delete("/roles/1")
    assert response.status_code == 200
