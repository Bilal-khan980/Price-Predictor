import requests


# Assuming Flask server is running locally on port 5000
url = 'http://localhost:5000/predict'


def test_predict():
    # Input data for testing
    data = {
        'sqft': 1500,
        'bedrooms': 3,
        'bathrooms': 2
    }
    
    # Sending POST request
    response = requests.post(url, data=data)
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the response contains the predicted price
    assert "Predicted House Price" in response.text


if __name__ == "__main__":
    test_predict()
