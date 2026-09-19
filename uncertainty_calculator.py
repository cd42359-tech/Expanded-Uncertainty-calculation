import streamlit as st
import numpy as np
import math

# =====================================================
# MASTER BUDGETS
# =====================================================

ALL_BUDGETS = {

    "Micrometer": {

        "0-25": [
            0.000173205,
            0.000050000,
            0.000288675,
            0.000046765,
            0.000007000,
            0.000023671,
            0.000098150
        ],

        "25-50": [
            0.000173205,
            0.000078000,
            0.000288675,
            0.000093531,
            0.000013500,
            0.000046765,
            0.000196299
        ],

        "50-75": [
            0.000173205,
            0.000086000,
            0.000288675,
            0.000140296,
            0.000020500,
            0.000070437,
            0.000294449
        ],

        "75-100": [
            0.000173205,
            0.000125500,
            0.000288675,
            0.000187061,
            0.000027000,
            0.000093531,
            0.000392598
        ]
    }
}

# =====================================================
# TEMPERATURE CONTRIBUTION
# =====================================================

def calculate_temperature_uncertainty(length_mm, temperature):

    alpha = 8.1e-6

    delta_t = abs(temperature - 20)

    temp_mm = alpha * delta_t * length_mm

    temp_um = temp_mm * 1000

    return temp_um / 1000


# =====================================================
# PAGE
# =====================================================

st.set_page_config(
    page_title="KEP Uncertainty Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 KEP Master Uncertainty Calculator")

# =====================================================
# INPUTS
# =====================================================

instrument = st.selectbox(
    "Select Instrument",
    list(ALL_BUDGETS.keys())
)

selected_range = st.selectbox(
    "Select Range",
    list(ALL_BUDGETS[instrument].keys())
)

r1 = st.number_input("Reading 1")
r2 = st.number_input("Reading 2")
r3 = st.number_input("Reading 3")
r4 = st.number_input("Reading 4")
r5 = st.number_input("Reading 5")

temperature = st.number_input(
    "Temperature (°C)",
    value=20.0,
    step=0.1
)

nominal_size = st.number_input(
    "Nominal Size (mm)",
    value=25.0
)

# =====================================================
# CALCULATE
# =====================================================

if st.button("Calculate Uncertainty"):

    readings = [r1, r2, r3, r4, r5]

    mean_value = np.mean(readings)

    std_dev = np.std(readings, ddof=1)

    u_repeat = std_dev / math.sqrt(5)

    fixed_budget = ALL_BUDGETS[instrument][selected_range]

    u_temp = calculate_temperature_uncertainty(
        nominal_size,
        temperature
    )

    contributors = [u_repeat]

    contributors.extend(fixed_budget)

    contributors.append(u_temp)

    uc = math.sqrt(
        sum(x**2 for x in contributors)
    )

    U = uc * 2

    # ==========================================
    # RESULTS
    # ==========================================

    st.subheader("Results")

    st.write(
        f"Mean Reading : {mean_value:.6f}"
    )

    st.write(
        f"Standard Deviation : {std_dev:.6f}"
    )

    st.write(
        f"Repeatability Uncertainty : {u_repeat:.6f}"
    )

    st.write(
        f"Temperature : {temperature:.1f} °C"
    )

    st.write(
        f"Temperature Deviation : {abs(temperature-20):.1f} °C"
    )

    st.write(
        f"Temperature Contribution : {u_temp:.6f}"
    )

    st.write(
        f"Combined Uncertainty (Uc) : {uc:.6f}"
    )

    st.success(
        f"Expanded Uncertainty U(k=2) = ±{U:.6f}"
    )

    st.subheader("Reported Result")

    st.success(
        f"{mean_value:.6f} ± {U:.6f}"
    )
    
import pandas as pd
df = pd.DataFrame({
    "Contributor": [
        "Repeatability",
        "Master Standard",
        "Resolution",
        "Temperature"
    ]
})

st.subheader("Uncertainty Contributors")
st.dataframe(df)
