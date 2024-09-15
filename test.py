"""
This module handles evaluation of the linear regression model and runs tests.
"""

import os
import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

MODEL_FILE = 'trained_model.pkl'
TEST_DATA_PATH = 'house_test_data.csv'


def fetch_test_data(file_path):
    """
    Fetches test data from the specified file path.

    Args:
        file_path (str): The path to the CSV file containing test data.

    Returns:
        tuple: A tuple containing two numpy arrays - features and labels.
    """
    dataset = pd.read_csv(file_path)
    features = dataset[['Size', 'Bedrooms', 'Bathrooms']].values
    labels = dataset['Price'].values
    return features, labels


def evaluate_trained_model():
    """
    Evaluates the trained model using the test data.

    Returns:
        tuple: A tuple containing the mean squared error and R2 score of the model.
    """
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError("Model not found! Train the model by running 'main.py'.")

    with open(MODEL_FILE, 'rb') as model_file:
        trained_model = pickle.load(model_file)

    test_features, test_labels = fetch_test_data(TEST_DATA_PATH)
    predictions = trained_model.predict(test_features)
    mse_value = mean_squared_error(test_labels, predictions)
    r2_value = r2_score(test_labels, predictions)
    
    return mse_value, r2_value


def test_fetch_test_data():
    """
    Tests the fetch_test_data function to ensure it returns non-empty results.
    """
    test_features, test_labels = fetch_test_data(TEST_DATA_PATH)
    assert len(test_features) > 0
    assert len(test_labels) > 0
    assert len(test_features) == len(test_labels)


def test_model_exists():
    """
    Tests the existence of the trained model file.
    """
    assert os.path.exists(MODEL_FILE)


def test_evaluate_trained_model():
    """
    Tests the evaluate_trained_model function to ensure it returns valid metrics.
    """
    mse_value, r2_value = evaluate_trained_model()
    assert isinstance(mse_value, float)
    assert isinstance(r2_value, float)
    assert 0 <= r2_value <= 1


if __name__ == "__main__":
    evaluate_trained_model()
