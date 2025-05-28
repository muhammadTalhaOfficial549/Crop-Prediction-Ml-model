import os
import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)

# Safe way to load the model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("🚨 Error loading model:", e)
    model = None

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return render_template("index.html", prediction_text="Model not loaded ❌")

        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return render_template("index.html", prediction_text=f"The Predicted Crop is {prediction[0]}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    flask_app.run(debug=True)
