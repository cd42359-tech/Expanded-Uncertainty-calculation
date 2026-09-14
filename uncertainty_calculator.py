import streamlit as st
import pandas as pd
import numpy as np

st.title("Calibration Uncertainty Calculator")

st.subheader("Caliper Uncertainty Calculation")
instrument = st.selectbox(
    "Select Instrument Type",
    ["Caliper"]
)
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
st.write("Nominal Size :", nominal_size)

st.write("Least Count :", least_count)
st.subheader("Input Measurements")
temp = st.number_input(
    "Temperature (°C)",
    value=20.0
)
r1 = st.number_input(
    "Reading 1",
    value=float(nominal_size)
)

r2 = st.number_input(
    "Reading 2",
    value=float(nominal_size)
)

r3 = st.number_input(
    "Reading 3",
    value=float(nominal_size)
)

r4 = st.number_input(
    "Reading 4",
    value=float(nominal_size)
)

r5 = st.number_input(
    "Reading 5",
    value=float(nominal_size)
)
readings = [r1, r2, r3, r4, r5]

mean_reading = np.mean(readings)
st.subheader("Measurement Summary")

summary_df = pd.DataFrame({
    "Parameter": [
        "Mean Reading",
        "Standard Deviation",
        "Repeatability U",
        "Error",
        "Resolution U"
    ],
    "Value": [
        round(mean_reading, 6),
        round(std_dev, 6),
        round(repeatability_u, 6),
        round(error, 6),
        round(resolution_u, 6)
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)

# Reference standard contributors from Caliper budget
# --------------------------------------------------
# Caliper Uncertainty Contributors
# --------------------------------------------------

if nominal_size == 150:

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000432

elif nominal_size == 200 and least_count == 0.01:

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000576

elif nominal_size == 200 and least_count == 0.02:

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000576

elif nominal_size == 300 and least_count == 0.01:

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000863

elif nominal_size == 300 and least_count == 0.02:

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000863

else:  # 600 mm (LC 0.02)

    acc_checker = 0.002887
    unc_checker = 0.001900
    temp_u = 0.000266


# --------------------------------------------------
# Display Contributors
# --------------------------------------------------

st.subheader("Uncertainty Budget Summary")

budget_df = pd.DataFrame({
    "Contributor": [
        "Repeatability U",
        "Resolution U",
        "Checker Accuracy U",
        "Checker Certificate U",
        "Temperature U"
    ],
    "Value": [
        round(repeatability_u, 6),
        round(resolution_u, 6),
        round(acc_checker, 6),
        round(unc_checker, 6),
        round(temp_u, 6)
    ]
})

st.dataframe(
    budget_df,
    use_container_width=True
)
combined_u = np.sqrt(
    repeatability_u**2 +
    resolution_u**2 +
    acc_checker**2 +
    unc_checker**2 +
    temp_u**2
)

expanded_u = 2 * combined_u
st.success(f"""
Combined Uncertainty : {combined_u:.6f}

Expanded Uncertainty : {expanded_u:.6f}
""")
