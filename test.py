import requests

# Assuming Flask server is running locally on port 5000
url = 'http://localhost:5000/predict'

# Input data for testing
data = {
    'sqft': 1500,
    'bedrooms': 3,
    'bathrooms': 2
}

# Sending POST request
response = requests.post(url, data=data)

# Printing response
print(response.text)
