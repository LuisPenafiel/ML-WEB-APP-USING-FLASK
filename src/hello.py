from flask import Flask, request, render_template
import numpy as np
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Define the path to the model file (absolute path for reliability)
MODEL_PATH = '/workspaces/ML-WEB-APP-USING-FLASK/src/iris_model_LR.pkl'

# Load the model with error handling
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}. Please ensure the file exists.")
    model = None
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Dictionary to map prediction indices to Iris class names
CLASS_DICT = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica",
    "Iris-versicolor": "Iris versicolor",
    "Iris-virginica": "Iris virginica"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error_message = None

    if request.method == 'POST':
        try:
            # Extract form values and convert to floats
            sepal_length = float(request.form['val1'])
            sepal_width = float(request.form['val2'])
            petal_length = float(request.form['val3'])
            petal_width = float(request.form['val4'])

            # Prepare input data for prediction
            input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

            # Check if model is loaded
            if model is None:
                error_message = "Model not loaded. Please check the server logs."
            else:
                # Make prediction
                prediction_idx = str(model.predict(input_data)[0])
                prediction = CLASS_DICT.get(prediction_idx, "Unknown class")

        except ValueError:
            error_message = "Invalid input: All values must be numbers."
        except Exception as e:
            error_message = f"Error during prediction: {str(e)}"

    # Render the template with the prediction or error message
    return render_template('index.html', prediction=prediction, error_message=error_message)

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 and port 5000 for dev container compatibility
    app.run(host='0.0.0.0', port=5000, debug=True)