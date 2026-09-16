import streamlit as st
import numpy as np
import math

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="KEP Uncertainty Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 KEP Standard Laboratory")
st.subheader("Master Uncertainty Calculator")

# --------------------------------------------------
# MICROMETER BUDGET
# Values taken from approved uncertainty worksheet
# --------------------------------------------------

MICROMETER_BUDGET = {

    "0-25": {
        "slip_accuracy": 0.000173205,
        "slip_uncertainty": 0.000050000,
        "resolution": 0.000288675,
        "temp_accuracy": 0.000046765,
        "temp_uncertainty": 0.000007000,
        "temp_difference": 0.000023671,
        "cte_difference": 0.000098150,
        "reference_temp": 0.000031177
    },

    "25-50": {
        "slip_accuracy": 0.000173205,
        "slip_uncertainty": 0.000078000,
        "resolution": 0.000288675,
        "temp_accuracy": 0.000093531,
        "temp_uncertainty": 0.000013500,
        "temp_difference": 0.000046765,
        "cte_difference": 0.000196299,
        "reference_temp": 0.000109119
    },

    "50-75": {
        "slip_accuracy": 0.000173205,
        "slip_uncertainty": 0.000086000,
        "resolution": 0.000288675,
        "temp_accuracy": 0.000140296,
        "temp_uncertainty": 0.000020500,
        "temp_difference": 0.000070437,
        "cte_difference": 0.000294449,
        "reference_temp": 0.000163390
    },

    "75-100": {
        "slip_accuracy": 0.000173205,
        "slip_uncertainty": 0.000125500,
        "resolution": 0.000288675,
        "temp_accuracy": 0.000187061,
        "temp_uncertainty": 0.000027000,
        "temp_difference": 0.000093531,
        "cte_difference": 0.000392598,
        "reference_temp": 0.000218238
    }

}

# --------------------------------------------------
# INSTRUMENT
# --------------------------------------------------

instrument = st.selectbox(
    "Select Instrument",
    [
        "Micrometer"
    ]
)

# --------------------------------------------------
# RANGE SELECTION
# --------------------------------------------------

selected_range = st.selectbox(
    "Select Micrometer Range",
    [
        "0-25",
        "25-50",
        "50-75",
        "75-100"
    ]
)

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

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

# --------------------------------------------------
# CALCULATE
# --------------------------------------------------

if st.button("Calculate"):

    readings = [r1, r2, r3, r4, r5]

    mean_value = np.mean(readings)

    std_dev = np.std(
        readings,
        ddof=1
    )

    u_repeat = std_dev / math.sqrt(5)

    budget = MICROMETER_BUDGET[selected_range]

    contributors = [

        u_repeat,

        budget["slip_accuracy"],
        budget["slip_uncertainty"],
        budget["resolution"],
        budget["temp_accuracy"],
        budget["temp_uncertainty"],
        budget["temp_difference"],
        budget["cte_difference"],
        budget["reference_temp"]

    ]

    uc = math.sqrt(
        sum(x**2 for x in contributors)
    )

    U = 2 * uc

    st.subheader("Results")

    st.write(
        f"Mean Reading = {mean_value:.6f} mm"
    )

    st.write(
        f"Standard Deviation = {std_dev:.6f}"
    )

    st.write(
        f"Repeatability Uncertainty = {u_repeat:.6f}"
    )

    st.write(
        f"Combined Uncertainty (Uc) = {uc:.6f}"
    )

    st.success(
        f"Expanded Uncertainty U(k=2) = ±{U:.6f} mm"
    )

    st.subheader("Reported Result")

    st.success(
        f"{mean_value:.6f} ± {U:.6f} mm"
    )
