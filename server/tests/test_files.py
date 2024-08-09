import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.api import app

# To do: add a files fixture

client = TestClient(app)

def test_list_files():
    response = client.get("/files")
    assert response.status_code == 200

def test_post_files():
    response = client.post("/files")
    assert response.status_code == 200

def test_read_file():
    response = client.get("/files/1")
    assert response.status_code == 200

def test_update_file():
    response = client.put("/files/1")
    assert response.status_code == 200

def test_delete_file():
    response = client.delete("/files/1")
    assert response.status_code == 200
