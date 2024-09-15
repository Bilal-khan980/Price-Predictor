import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

MODEL_PATH = 'model.pkl'
CSV_FILE_PATH = 'house_data.csv'


def load_data_from_csv(file_path):
    """Load dataset from a CSV file."""
    data = pd.read_csv(file_path)
    house_sizes = data[['Size', 'Bedrooms', 'Bathrooms']].values
    house_prices = data['Price'].values
    return house_sizes, house_prices


def train_model():
    """Train a linear regression model on house data and save the model."""
    house_sizes, house_prices = load_data_from_csv(CSV_FILE_PATH)

    model = LinearRegression()
    model.fit(house_sizes, house_prices)

    with open(MODEL_PATH, 'wb') as file:
        pickle.dump(model, file)

    print("Model training complete. Model saved to 'model.pkl'.")


if __name__ == "__main__":
    train_model()
