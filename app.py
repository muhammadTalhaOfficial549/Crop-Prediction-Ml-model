import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values and convert to float
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]

        # Predict
        prediction = model.predict(features)

        # Return prediction to the web page
        return render_template("index.html", prediction_text=f"The Predicted Crop is {prediction[0]}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    flask_app.run(debug=True)
