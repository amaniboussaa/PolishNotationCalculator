from fastapi.testclient import TestClient
from api.main import app
from fastapi import status

client = TestClient(app)

def test_calculate():
    response = client.post("/calculate/", params={"expression": "3 4 +"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"expression": "3 4 +", "result": 7}

def test_export_csv():
    response = client.get("/export/")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]

