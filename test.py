import requests
import subprocess
import time
import signal
import os

url = 'http://localhost:5000/predict'

def start_server():
    # Start the Flask server as a background process
    process = subprocess.Popen(['flask', 'run', '--host=0.0.0.0', '--port=5000'], 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
    time.sleep(5)  # Wait for server to start
    return process

def stop_server(process):
    # Stop the Flask server
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)

def test_predict():
    # Start the server
    process = start_server()
    
    try:
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
    finally:
        # Stop the server after the test
        stop_server(process)

if __name__ == "__main__":
    test_predict()
