import pytest
from app import app
import json

@pytest.fixture
def client():
    """Fixture to configure the test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test if the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>House Price Predictor</h1>' in response.data
    assert b'Predict Price' in response.data

def test_predict_valid(client):
    """Test the /predict route with valid inputs."""
    response = client.post('/predict', data={
        'sqft': '1500',
        'bedrooms': '3',
        'bathrooms': '2'
    })
    assert response.status_code == 200
    assert b'Predicted House Price' in response.data

def test_predict_invalid(client):
    """Test the /predict route with invalid inputs."""
    response = client.post('/predict', data={
        'sqft': 'invalid_value',
        'bedrooms': '3',
        'bathrooms': '2'
    })
    assert response.status_code == 200  # Flask should return 200, but with an error message
    assert b'error' in response.data
