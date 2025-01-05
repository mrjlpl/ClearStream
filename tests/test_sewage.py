from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_create_sewage():
    response = client.post("/sewages/", json={"name": "Test Sewage", "description": "Test Description", "flow_rate": 1.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Sewage"

def test_read_sewages():
    response = client.get("/sewages/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
