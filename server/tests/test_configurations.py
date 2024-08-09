from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_configurations():
    response = client.get("/configurations")
    assert response.status_code == 200


def test_post_configurations():
    response = client.post("/configurations")
    assert response.status_code == 200


def test_get_configuration():
    response = client.get("/configurations/1")
    assert response.status_code == 200


def test_update_configuration():
    response = client.put("/configurations/1")
    assert response.status_code == 200


def test_delete_configuration():
    response = client.delete("/configurations/1")
    assert response.status_code == 200
