from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    r = client.post("/predict", json={
        "sepal_length": 5.1, "sepal_width": 3.5,
        "petal_length": 1.4, "petal_width": 0.2})
    assert r.status_code == 200
    assert "class" in r.json()