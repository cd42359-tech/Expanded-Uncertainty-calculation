import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model
model = joblib.load("uncertainty_model.pkl")

st.title("Calibration Uncertainty Prediction System")

# --------------------------------------------------
# Instrument Selection
# --------------------------------------------------

instrument = st.selectbox(
    "Select Instrument Type",
    ["Caliper", "Micrometer", "Plug Gauge", "Plunger Dial"]
)

# --------------------------------------------------
# Nominal Size Selection
# --------------------------------------------------

if instrument == "Caliper":

    option = st.selectbox(
        "Select Nominal Size",
        [
            "150 mm (LC 0.01)",
            "200 mm (LC 0.01)",
            "200 mm (LC 0.02)",
            "300 mm (LC 0.01)",
            "300 mm (LC 0.02)",
            "600 mm (LC 0.02)"
        ]
    )

    if option == "150 mm (LC 0.01)":
        nominal_size = 150
        least_count = 0.01

    elif option == "200 mm (LC 0.01)":
        nominal_size = 200
        least_count = 0.01

    elif option == "200 mm (LC 0.02)":
        nominal_size = 200
        least_count = 0.02

    elif option == "300 mm (LC 0.01)":
        nominal_size = 300
        least_count = 0.01

    elif option == "300 mm (LC 0.02)":
        nominal_size = 300
        least_count = 0.02

    else:
        nominal_size = 600
        least_count = 0.02

elif instrument == "Micrometer":

    nominal_size = st.selectbox(
        "Select Nominal Size",
        [25, 50, 75, 100]
    )

    least_count = 0.001

elif instrument == "Plug Gauge":

    nominal_size = st.selectbox(
        "Select Nominal Size",
        [5.961, 20.4886, 50.822]
    )

    least_count = 0

else:

    nominal_size = st.selectbox(
        "Select Nominal Size",
        [1, 10]
    )

    if nominal_size == 1:
        least_count = 0.001
    else:
        least_count = 0.01

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

temp = st.number_input(
    "Temperature (°C)",
    value=20.0
)

st.subheader("Enter Five Readings")

r1 = st.number_input("Reading 1")
r2 = st.number_input("Reading 2")
r3 = st.number_input("Reading 3")
r4 = st.number_input("Reading 4")
r5 = st.number_input("Reading 5")

# --------------------------------------------------
# Auto Calculations
# --------------------------------------------------

readings = [r1, r2, r3, r4, r5]

mean_reading = np.mean(readings)

std_dev = np.std(readings, ddof=1)

repeatability_u = std_dev / np.sqrt(5)

error = mean_reading - nominal_size

# --------------------------------------------------
# Display Calculated Values
# --------------------------------------------------

st.subheader("Calculated Parameters")

st.write(f"Least Count : {least_count}")

st.write(f"Mean Reading : {mean_reading:.6f}")

st.write(f"Standard Deviation : {std_dev:.6f}")

st.write(f"Repeatability Uncertainty : {repeatability_u:.6f}")

st.write(f"Error : {error:.6f}")

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Expanded Uncertainty"):

    input_data = pd.DataFrame({
        "Nominal size": [nominal_size],
        "Least count": [least_count],
        "Temp": [temp],
        "Std_Dev": [std_dev],
        "Repeatability_U": [repeatability_u],
        "Error": [error]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Expanded Uncertainty : {prediction[0]:.6f}"
    )
