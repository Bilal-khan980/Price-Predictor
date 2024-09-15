import pytest
from app import app  # Import your Flask app here

# Create a test client using the Flask app
client = app.test_client()


def test_predict():
    # Input data for testing
    data = {
        'sqft': 1500,
        'bedrooms': 3,
        'bathrooms': 2
    }

    # Sending POST request
    response = client.post('/predict', data=data)
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the response contains the predicted price
    assert "Predicted House Price" in response.data.decode()


if __name__ == "__main__":
    pytest.main()
