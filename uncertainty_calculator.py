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
