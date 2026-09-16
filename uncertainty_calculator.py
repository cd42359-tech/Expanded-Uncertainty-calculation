import streamlit as st
import pandas as pd
import math

st.set_page_config(
    page_title="KEP Uncertainty Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 KEP Standard Laboratory")
st.subheader("Master Uncertainty Calculator")

# -------------------------------
# Common Function
# -------------------------------

def calculate_uncertainty(contributors):

    uc = math.sqrt(sum(u**2 for u in contributors))
    U = 2 * uc

    return uc, U


# -------------------------------
# Instrument Selection
# -------------------------------

instrument = st.selectbox(
    "Select Instrument",
    [
        "Micrometer",
        "Vernier Caliper",
        "Dial Gauge",
        "Plug Gauge",
        "Plunger Dial"
    ]
)

st.divider()

# -------------------------------
# Inputs
# -------------------------------

repeatability = st.number_input(
    "Repeatability Contribution",
    value=0.0000,
    format="%.6f"
)

resolution = st.number_input(
    "Resolution",
    value=0.0000,
    format="%.6f"
)

certificate = st.number_input(
    "Master/Certificate Uncertainty",
    value=0.0000,
    format="%.6f"
)

temperature = st.number_input(
    "Temperature Contribution",
    value=0.0000,
    format="%.6f"
)

# -------------------------------
# Calculate Button
# -------------------------------

if st.button("Calculate"):

    u_repeat = repeatability

    u_resolution = resolution / math.sqrt(12)

    u_certificate = certificate / 2

    u_temperature = temperature / math.sqrt(3)

    contributors = [
        u_repeat,
        u_resolution,
        u_certificate,
        u_temperature
    ]

    uc, U = calculate_uncertainty(contributors)

    budget = pd.DataFrame({
        "Contributor": [
            "Repeatability",
            "Resolution",
            "Certificate",
            "Temperature"
        ],
        "Standard Uncertainty": [
            u_repeat,
            u_resolution,
            u_certificate,
            u_temperature
        ]
    })

    st.subheader("Uncertainty Budget")
    st.dataframe(budget, use_container_width=True)

    st.success(
        f"Combined Uncertainty (Uc) = {uc:.6f}"
    )

    st.success(
        f"Expanded Uncertainty U(k=2) = ±{U:.6f}"
    )
