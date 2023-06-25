from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_users():
    response = client.get('/users', params={'token': 'jessica'})
    assert response.status_code == 200
    assert {"username": "Rick"} in response.json()
    assert {"username": "Morty"} in response.json()

def test_update_items():
    response = client.put(
        '/items/plumbus?token=jessica', 
        headers={"X-Token": "fake-super-secret-token"},
        )
    assert response.status_code == 200
    assert response.json() == {"item_id": "plumbus", "name": "The great Plumbus"}
