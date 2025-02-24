import sys
import os

# Ensure the tests can find main.py
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from main import app  # Import FastAPI app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
