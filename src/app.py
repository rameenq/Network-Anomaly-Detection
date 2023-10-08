from flask import Flask, request, jsonify, render_template
import joblib  # To load the trained machine learning model
import numpy as np  # For numerical operations
import os

app = Flask(__name__)

# Check if the model file exists
model_path = "../notebooks/isolation_forest_model.pkl"
scaler_path = "../notebooks/scaler.pkl" 
if os.path.exists(model_path):
    print("File exists.")
    # Load the trained model
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
else:
    print("File does not exist.")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Handle JSON payload
            if request.is_json:
                data = request.json
            # Handle form payload
            else:
                data = request.form.to_dict()

            # Extract features from form
            timestamp = float(data['Timestamp'])
            status = float(data['Status'])
            method_delete = float(data['Method_DELETE'])
            method_get = float(data['Method_GET'])
            method_post = float(data['Method_POST'])
            method_put = float(data['Method_PUT'])

            # Combine into a single numpy array
            features = np.array([timestamp, status, method_delete, method_get, method_post, method_put])

            print("Received feature list:", features)

            # Apply scaling
            features_scaled = scaler.transform([features])

            print("Features after scaling:", features_scaled)

            # Make a prediction
            prediction = model.predict(features_scaled)

            # Translate prediction into a user-friendly message
            prediction_message = "Anomaly detected" if prediction[0] == -1 else "Normal data point"

            print("Model prediction:", prediction)

            return render_template('results.html', prediction=prediction[0], prediction_message=prediction_message)

        except Exception as e:
            print("Exception occurred:", str(e))  # Debugging print
            return render_template('error.html', error=str(e))



if __name__ == '__main__':  
    app.run(debug=True)



