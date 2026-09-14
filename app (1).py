
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("uncertainty_model.pkl")

st.title("Calibration Uncertainty Prediction System")

st.write("Enter calibration parameters")

nominal_size = st.number_input("Nominal Size", value=100.0)
least_count = st.number_input("Least Count", value=0.01)
temp = st.number_input("Temperature", value=20.0)
std_dev = st.number_input("Standard Deviation", value=0.001)
repeatability_u = st.number_input("Repeatability Uncertainty", value=0.0005)
error = st.number_input("Error", value=0.001)

if st.button("Predict Expanded Uncertainty"):

    input_data = pd.DataFrame({
        'Nominal size': [nominal_size],
        'Least count': [least_count],
        'Temp': [temp],
        'Std_Dev': [std_dev],
        'Repeatability_U': [repeatability_u],
        'Error': [error]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Expanded Uncertainty: {prediction[0]:.6f}"
    )
