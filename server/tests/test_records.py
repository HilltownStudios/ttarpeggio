from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_list_records():
    response = client.get("/records")
    assert response.status_code == 200


def test_post_records():
    response = client.post("/records")
    assert response.status_code == 200


def test_get_record():
    response = client.get("/records/1")
    assert response.status_code == 200


def test_update_record():
    response = client.put("/records/1")
    assert response.status_code == 200


def test_delete_record():
    response = client.delete("/records/1")
    assert response.status_code == 200
