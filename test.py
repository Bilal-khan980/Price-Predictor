import requests
import subprocess
import time


# Assuming Flask server is running locally on port 5000
url = 'http://localhost:5000/predict'

def start_server():
    # Start the Flask server in the background
    subprocess.Popen(['flask', 'run', '--host=0.0.0.0', '--port=5000'])
    # Give the server a few seconds to start
    time.sleep(5)

def test_predict():
    start_server()
    
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
