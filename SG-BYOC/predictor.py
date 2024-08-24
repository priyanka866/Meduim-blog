from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Pre-trained model 
model = LinearRegression()
model.coef_ = np.array([2.0])  
model.intercept_ = 1.0 

@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

@app.route('/invocations', methods=['POST'])
def invocations():
    # Parse input
    input_json = request.get_json()
    input_data = pd.DataFrame(input_json)

    # Check if the input data has the expected structure
    if "feature" not in input_data.columns:
        return jsonify({"error": "Missing required feature column"}), 400

    # Perform prediction
    predictions = model.predict(input_data[['feature']])

    # Return the predictions as JSON
    result = {"predictions": predictions.tolist()}
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
