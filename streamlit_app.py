import streamlit as st
import numpy as np
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction features to predict fraud")

features = []

# create inputs
for i in range(29):
    value = st.number_input(f"Feature V{i+1}", value=0.0)
    features.append(value)

if st.button("Predict Transaction"):

    features_array = np.array(features).reshape(1, -1)

    prediction = model.predict(features_array)

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")

    # SHAP explanation
 # SHAP explanation
st.subheader("Model Explanation (SHAP)")

import shap
import matplotlib.pyplot as plt

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(features_array)

feature_names = [f"V{i+1}" for i in range(29)]

# Handle both SHAP output formats
if isinstance(shap_values, list):
    vals = shap_values[0]
else:
    vals = shap_values

fig, ax = plt.subplots()

shap.summary_plot(
    vals,
    features_array,
    feature_names=feature_names,
    show=False
)

st.pyplot(fig)