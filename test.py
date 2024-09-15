from app import app

def test_predict():
    client = app.test_client()
    data = {
        'sqft': 1500,
        'bedrooms': 3,
        'bathrooms': 2
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert "Predicted House Price" in response.data.decode()

if __name__ == "__main__":
    import pytest
    pytest.main()
