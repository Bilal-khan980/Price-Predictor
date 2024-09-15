"""
This module serves a linear regression model using Flask.
"""

import os
import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

MODEL_FILE_PATH = 'trained_model.pkl'

try:
    if os.path.exists(MODEL_FILE_PATH):
        with open(MODEL_FILE_PATH, 'rb') as model_file:
            model = pickle.load(model_file)
    else:
        raise FileNotFoundError("Model file not found. Please run 'main.py' to train the model.")
except (FileNotFoundError, IOError, pickle.UnpicklingError):
    model = None


@app.route('/')
def home_page():
    """
    Renders the home page of the web application.
    """
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def predict():
    """
    Predicts the price based on input features provided in the POST request.

    Returns:
        json: The predicted price or an error message.
    """
    if model is None:
        return jsonify({"error": "Model is not loaded. Train the model first."}), 500

    try:
        request_data = request.get_json()
        feature_size = float(request_data.get('size', 0))
        feature_bedrooms = int(request_data.get('bedrooms', 0))
        feature_bathrooms = int(request_data.get('bathrooms', 0))

        if feature_size <= 0 or feature_bedrooms < 0 or feature_bathrooms < 0:
            raise ValueError("Invalid input values for size, bedrooms, or bathrooms.")

        feature_array = np.array([[feature_size, feature_bedrooms, feature_bathrooms]])
        prediction = model.predict(feature_array)[0]

        return jsonify({"predicted_price": prediction})

    except (ValueError, KeyError):
        return jsonify({"error": "Invalid input values."}), 400

    except (FileNotFoundError, IOError, pickle.UnpicklingError):
        return jsonify({"error": "Model loading error."}), 500

    except (TypeError, AttributeError):
        return jsonify({"error": "Unexpected error occurred."}), 500


if __name__ == "__main__":
    app.run(debug=True)
