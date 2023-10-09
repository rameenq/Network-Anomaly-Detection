# Network-Anomaly-Detection

## Anomaly Detection Web App

### Table of Contents
- [**Overview**](#overview)
- [**Features**](#features)
- [**Requirements**](#requirements)
- [**Installation**](#installation)
- [**Usage**](#usage)
- [**Directory Structure**](#directory-structure)
- [**Future improvements**](#future-improvements)
- [**Contributing**](#contributing)

### Overview

This web app is designed to perform real-time anomaly detection using machine learning. It uses Flask for the backend and is based on an Isolation Forest model trained on network activity data. Users can input various features related to network activity, such as Timestamp, HTTP Status Codes, and HTTP Methods, to predict if the given data point is an anomaly.

### Features
- **Real-Time Anomaly Detection:** Immediate predictions on user input.
- **Feature Scaling:** Employs data normalization for more accurate predictions.
- **Robust Exception Handling:** Designed to be resilient against unexpected data or behavior.

### Requirements

- Python 3.x
- Flask
- NumPy
- joblib
  
### Installation

1. Clone this repository to your local machine: 
   ``` git clone https://github.com/rameenq/Network-Anomaly-Detection.git ```
   
2. Navigate to the directory containing requirements.txt and run:
   ``` pip install -r requirements.txt.```
   
### Usage
1. Navigate to the root directory of the project.
2. Run:
   ``` python app.py.```
3. Open a web browser and go to http://localhost:5000/ to access the web interface.
4. Open the web interface.
2. Enter the required features (Timestamp, HTTP Status Codes, HTTP Methods) into the form. You can generate a sample data set by running the test_model.py file:
   ``` python test_model.py```
3. Click on the "Predict" button.
4. The result will be displayed, indicating whether the data point is an anomaly or not.
   
### Directory Structure
- data/ : Contains the python and csv files used to generate synthetic logs which were used to train the model.
- src/app.py : The main Flask app script.
- templates/ : Contains the HTML templates.
- notebooks/ : Contains the trained Isolation Forest model (isolation_forest_model.pkl) and the scaler (scaler.pkl).
  
### Future Improvements
- Add real-time updates using WebSockets.
- Automate the process of data collection for continuous monitoring.

### Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

