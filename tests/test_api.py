from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_api_contract():
    customer = {
        "tenure_months": 5,
        "monthly_fee": 89.9,
        "contract": "one-year",
        "internet_service": "fiber",
        "support_calls": 2
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200
    assert "churn_probability" in response.json()
    assert isinstance(response.json()["churn_probability"], float) 
    
def test_model_loads():
    from src.app.main import model
    assert model is not None
    assert hasattr(model, "predict_proba")

def test_input_schema():
    customer = {
        "tenure_months": -5,
        "monthly_fee": 89.9,
        "contract": "one-year",
        "internet_service": "fiber",
        "support_calls": 2
    }

    response = client.post("/predict", json=customer)
    assert response.status_code == 422

def test_edge_case():
    customer = {
        "tenure_months": 0,
        "monthly_fee": 0,
        "contract": "one-year",
        "internet_service": "fiber",
        "support_calls": 0
    }

    response = client.post("/predict", json=customer)
    assert response.status_code == 200
    assert "churn_probability" in response.json()

def test_deterministic_prediction():
    customer = {
        "tenure_months": 5,
        "monthly_fee": 89.9,
        "contract": "one-year",
        "internet_service": "fiber",
        "support_calls": 2
    }

    response1 = client.post("/predict", json=customer)
    response2 = client.post("/predict", json=customer)

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()