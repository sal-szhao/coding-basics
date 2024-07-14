'''
Simple fast-api pytest file for testing Github Actions to realize
continuous integration (CI). 
'''

from fastapi.testclient import TestClient

from ci import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}