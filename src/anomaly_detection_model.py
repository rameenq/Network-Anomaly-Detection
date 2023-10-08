import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import joblib

def load_data(filepath):
    """Load and preprocess the dataset."""
    # Load the data
    data = pd.read_csv(filepath)
    
    # Identify numeric columns
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    
    # Apply scaling only to numeric columns
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    return data[numeric_cols]

def load_model(model_path):
    """Load the pre-trained model."""
    return joblib.load(model_path)

def predict_anomalies(model, data):
    """Make predictions and calculate anomaly scores."""
    # Make predictions (-1 for anomalies and 1 for normal points)
    predictions = model.predict(data)
    
    # Calculate anomaly scores
    anomaly_score = model.decision_function(data)
    
    return predictions, anomaly_score

if __name__ == "__main__":
    # Filepaths
    new_data_filepath = '../data/logs_train.csv'  # Replace with the path to the new data
    model_filepath = '../notebooks/isolation_forest_model.pkl'  # Replace with the path to the saved model
    
    # Load and preprocess new data
    new_data = load_data(new_data_filepath)
    
    # Load the pre-trained model
    model = load_model(model_filepath)
    
    # Make predictions and calculate anomaly scores
    predictions, anomaly_scores = predict_anomalies(model, new_data)
    
    print("Predictions:", predictions)
    print("Anomaly Scores:", anomaly_scores)
