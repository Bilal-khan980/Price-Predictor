from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd  # Import pandas to handle data formatting

app = Flask(__name__)


model = joblib.load('house_price_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [float(x) for x in request.form.values()]

        # Ensure the input is formatted correctly as a DataFrame
        columns = ['sqft', 'bedrooms', 'bathrooms']
        final_features = pd.DataFrame([features], columns=columns)

        # Make prediction
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)
        return render_template(
            'index.html',
            prediction_text=f'Predicted House Price: ${output}'
        )

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
