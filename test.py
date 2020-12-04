# mypy: no-disallow-untyped-decorators
# pylint: disable=E0611
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["db.models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


def test_create_field(client: TestClient):  # nosec
    response = client.post("/fields/", json={"name": "Carichan"})
    assert response.status_code == 200, response.text
    data = response.json()
    id = data["id"]
    print(f'ID IS {id}')
    assert id == 1
