from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/model.pkl")


@app.route("/")
def home():
    return "Credit Card Fraud Detection API"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["features"]

    features = np.array(data).reshape(1, -1)

    prediction = model.predict(features)

    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)