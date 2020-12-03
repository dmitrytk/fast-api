from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world!'}


def test_read_main2():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world!'}
