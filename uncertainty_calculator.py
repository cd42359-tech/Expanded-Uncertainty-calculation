import streamlit as st
import pandas as pd
import numpy as np
import math

# ----------------------------------
# Page Setup
# ----------------------------------

st.set_page_config(
    page_title="KEP Uncertainty Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 KEP Standard Laboratory")
st.subheader("Master Uncertainty Calculator")

# ----------------------------------
# Budget Database
# (Temporary values)
# ----------------------------------

BUDGETS = {
    "Micrometer": {
        "resolution": 0.000289,
        "master": 0.000500,
        "temp_coeff": 0.000200
    },

    "Vernier Caliper": {
        "resolution": 0.005000,
        "master": 0.002000,
        "temp_coeff": 0.001000
    },

    "Dial Gauge": {
        "resolution": 0.001000,
        "master": 0.001500,
        "temp_coeff": 0.000500
    },

    "Plug Gauge": {
        "resolution": 0.000000,
        "master": 0.000300,
        "temp_coeff": 0.000100
    }
}

# ----------------------------------
# Instrument Selection
# ----------------------------------

instrument = st.selectbox(
    "Select Instrument",
    [
        "Micrometer",
        "Vernier Caliper",
        "Dial Gauge",
        "Plug Gauge"
    ]
)

# ----------------------------------
# Inputs
# ----------------------------------

nominal = st.number_input(
    "Nominal Size (mm)",
    value=25.000,
    format="%.3f"
)

r1 = st.number_input("Reading 1", format="%.6f")
r2 = st.number_input("Reading 2", format="%.6f")
r3 = st.number_input("Reading 3", format="%.6f")
r4 = st.number_input("Reading 4", format="%.6f")
r5 = st.number_input("Reading 5", format="%.6f")

temperature = st.number_input(
    "Temperature (°C)",
    value=20.0,
    format="%.1f"
)

# ----------------------------------
# Calculate
# ----------------------------------

if st.button("Calculate"):

    readings = [r1, r2, r3, r4, r5]

    mean_value = np.mean(readings)

    std_dev = np.std(readings, ddof=1)

    u_repeat = std_dev / np.sqrt(len(readings))

    selected_budget = BUDGETS[instrument]

    u_resolution = selected_budget["resolution"]

    u_master = selected_budget["master"]

    u_temp = selected_budget["temp_coeff"]

    uc = math.sqrt(
        u_repeat**2 +
        u_resolution**2 +
        u_master**2 +
        u_temp**2
    )

    U = 2 * uc

    st.subheader("Results")

    st.write(f"Mean Reading = {mean_value:.6f}")

    st.write(f"Standard Deviation = {std_dev:.6f}")

    st.write(f"Repeatability Uncertainty = {u_repeat:.6f}")

    st.write(f"Combined Uncertainty (Uc) = {uc:.6f}")

    st.success(
        f"Expanded Uncertainty U(k=2) = ±{U:.6f} mm"
    )
