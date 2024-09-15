"""
This module trains a linear regression model on housing data.
"""
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

MODEL_SAVE_PATH = 'trained_model.pkl'
DATA_FILE_PATH = 'house_data.csv'


def fetch_data(file_path):
    """Loads housing data from a CSV file."""
    dataset = pd.read_csv(file_path)
    features = dataset[['Size', 'Bedrooms', 'Bathrooms']].values
    labels = dataset['Price'].values
    return features, labels


def build_and_train_model():
    """Builds and trains a linear regression model on the housing dataset."""
    feature_data, target_values = fetch_data(DATA_FILE_PATH)

    regressor = LinearRegression()
    regressor.fit(feature_data, target_values)

    with open(MODEL_SAVE_PATH, 'wb') as model_file:
        pickle.dump(regressor, model_file)


if __name__ == "__main__":
    build_and_train_model()
