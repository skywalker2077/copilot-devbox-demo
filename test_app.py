import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["version"] == "1.0"


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json == {"status": "ok", "version": "1.0"}