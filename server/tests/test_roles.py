from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_roles():
    response = client.get("/roles")
    assert response.status_code == 200


def test_post_roles():
    response = client.post("/roles")
    assert response.status_code == 200


def test_get_role():
    response = client.get("/roles/1")
    assert response.status_code == 200


def test_update_role():
    response = client.put("/roles/1")
    assert response.status_code == 200


def test_delete_role():
    response = client.delete("/roles/1")
    assert response.status_code == 200
