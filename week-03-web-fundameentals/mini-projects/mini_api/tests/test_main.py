import pytest
from fastapi.testclient import TestClient
import app.main as main
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse = True)
def reset_database():
    main.products = [
        {"product_id" : 101, "name" : "Dust pan", "category" : "cleaning" , "in_stock" : True},
        {"product_id": 102, "name" : "pen", "category" : "stationary" , "in_stock" : False},
        {"product_id": 103, "name" : "flower vase", "category" : "decoration", "in_stock" : True}
    ]


def test_get_all_products():
    response = client.get("/products")
    assert response.status_code == 200 


def test_get_a_product():
    product_id = 101
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Dust pan"

def test_add_product_success():
    response = client.post("/products", json = {"name" : "eraser", "category" : "stationary", "in_stock" : True})
    assert response.status_code == 201
    assert "104" in response.json()["message"]

def test_add_product_duplicate_failed():
    response = client.post("/products", json={"name" : "pen", "category" : "stationary", "in_stock" : True})
    assert response.status_code == 201
    


    