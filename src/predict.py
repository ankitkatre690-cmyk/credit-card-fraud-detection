import joblib
import numpy as np

model = joblib.load("../models/model.pkl")


def predict_transaction(features):

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    return prediction[0]