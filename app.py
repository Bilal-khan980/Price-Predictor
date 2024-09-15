from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Predict price based on input data
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]

        # Use the loaded model to predict the result
        prediction = model.predict(final_features)

        # Convert the prediction to an integer (house price)
        output = round(prediction[0], 2)
        return render_template('index.html', 
                       prediction_text=f'Predicted House Price: ${output}')

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
