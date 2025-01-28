from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    recency = float(request.form['Recency'])
    frequency = float(request.form['Frequency'])
    monetary = float(request.form['Monetary'])
    rfms_score = float(request.form['RFMS_Score'])

    # Create a DataFrame with the input features
    input_data = pd.DataFrame({
        'Recency': [recency],
        'Frequency': [frequency],
        'Monetary': [monetary],
        'RFMS_Score': [rfms_score]
    }, index=[0])

    # Make prediction
    prediction = model.predict(input_data)[0]  # Directly get the predicted class (0 or 1)

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)