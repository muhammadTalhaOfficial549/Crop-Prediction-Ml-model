# 🌾 Crop Prediction Web Application

This is a beginner-level Machine Learning project that predicts the most suitable crop to grow based on soil and weather conditions. It uses a trained ML model and is deployed using Flask as a simple web application.

---

## 🚀 How It Works

1. **User inputs** values for:
   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Temperature
   - Humidity
   - pH
   - Rainfall

2. The inputs are sent to a Flask backend.
3. The trained ML model (Decision Tree Classifier) processes the data.
4. The model predicts and displays the best crop to grow.

---

## 🧠 Technologies Used

- Python
- Scikit-learn
- Flask
- HTML/CSS
- Pickle
- Google Colab (for training model)

---

## 🗂️ Project Structure

Crop-Prediction/
│
├── static/
│ ├── style.css # Web page styling
│ └── farm.jpg # Background image
│
├── templates/
│ └── index.html # Web interface (input form)
│
├── model.py # ML training script
├── models.pkl # Trained model (pickle file)
├── app.py # Flask server
├── requirements.txt # List of Python libraries

HOW TO RUN:
 first save files in require folder as html file in templates folder and css and farm picture files in static folder
then first install the libraries and then run model.py
after that model.pkl file create then in app.py write in terminal python app.py (enter) then link will share click them and you see the project
