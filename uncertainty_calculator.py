import streamlit as st
import numpy as np
import math
ALL_BUDGETS = {

    # ==================================================
    # MICROMETER
    # ==================================================

    "Micrometer": {

        "0-25": [
            0.000173205,
            0.000050000,
            0.000288675,
            0.000046765,
            0.000007000,
            0.000023671,
            0.000098150,
            0.000031177
        ],

        "25-50": [
            0.000173205,
            0.000078000,
            0.000288675,
            0.000093531,
            0.000013500,
            0.000046765,
            0.000196299,
            0.000109119
        ],

        "50-75": [
            0.000173205,
            0.000086000,
            0.000288675,
            0.000140296,
            0.000020500,
            0.000070437,
            0.000294449,
            0.000163390
        ],

        "75-100": [
            0.000173205,
            0.000125500,
            0.000288675,
            0.000187061,
            0.000027000,
            0.000093531,
            0.000392598,
            0.000218238
        ]
    },

    # ==================================================
    # CALIPER
    # ==================================================

    "Caliper": {

        "0-150": [
            0.002886751,
            0.001900000,
            0.000635085,
            0.001000000,
            0.000115470,
            0.000500000,
            0.000288675,
            0.000350000,
            0.000173205,
            0.000050000,
            0.002886751,
            0.000199186,
            0.000058000,
            0.000199186,
            0.000049652,
            0.000431858
        ],

        "0-200": [
            0.002886751,
            0.001900000,
            0.000635085,
            0.001000000,
            0.000115470,
            0.000500000,
            0.000288675,
            0.000350000,
            0.000173205,
            0.000050000,
            0.002886751,
            0.000265581,
            0.000077000,
            0.000265581,
            0.000066395,
            0.000575618
        ],

        "0-300": [
            0.002886751,
            0.001900000,
            0.000635085,
            0.001000000,
            0.000115470,
            0.000500000,
            0.000288675,
            0.000350000,
            0.000173205,
            0.000050000,
            0.002886751,
            0.000398372,
            0.000115500,
            0.000398372,
            0.000099882,
            0.000863139
        ],

        "0-600": [
            0.002886751,
            0.001900000,
            0.000750555,
            0.001250000,
            0.000115470,
            0.000500000,
            0.000288675,
            0.000350000,
            0.000173205,
            0.000050000,
            0.005773503,
            0.000796743,
            0.000231000,
            0.000796743,
            0.000199186,
            0.002655811
        ]
    },

    # ==================================================
    # PLUG GAUGE
    # ==================================================

    "Plug Gauge": {

        "5.961": [
            0.000288675,
            0.000250000,
            0.000028868,
            0.000006928,
            0.000013279,
            0.000002000,
            0.000011547,
            0.000001732
        ],

        "20.4886": [
            0.000288675,
            0.000250000,
            0.000028868,
            0.000023094,
            0.000046188,
            0.000006500,
            0.000040415,
            0.000005774
        ],

        "50.822": [
            0.000244949,
            0.000091924,
            0.000028868,
            0.000057735,
            0.000114893,
            0.000016500,
            0.000099882,
            0.000028868
        ]
    },

    # ==================================================
    # PLUNGER DIAL
    # ==================================================

    "Plunger Dial": {

        "0-1": [
            0.000577350,
            0.000200000,
            0.000028868,
            0.000288675,
            0.000002887,
            0.000000500,
            0.000001155,
            0.000000577,
            0.000001155
        ],

        "0-10": [
            0.001616581,
            0.000200000,
            0.000028868,
            0.002886751,
            0.000026558,
            0.000004000,
            0.000013279,
            0.000003464,
            0.000010970
        ]
    }
}

st.set_page_config(
    page_title="KEP Uncertainty Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 KEP Master Uncertainty Calculator")

instrument = st.selectbox(
    "Select Instrument",
    list(ALL_BUDGETS.keys())
)

selected_range = st.selectbox(
    "Select Range",
    list(ALL_BUDGETS[instrument].keys())
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

if st.button("Calculate"):

    readings = [r1, r2, r3, r4, r5]

    mean_value = np.mean(readings)

    std_dev = np.std(readings, ddof=1)

    u_repeat = std_dev / math.sqrt(5)

    budget = ALL_BUDGETS[instrument][selected_range]

    # Temperature difference from 20°C
    delta_t = abs(temperature - 20.0)

    # Keep all contributors except last one
    fixed_contributors = budget[:-1]

    # Dynamic temperature contribution
    dynamic_temp = budget[-1] * delta_t

    contributors = (
        [u_repeat]
        + fixed_contributors
        + [dynamic_temp]
    )

    uc = math.sqrt(
        sum(x**2 for x in contributors)
    )

    U = 2 * uc

    st.subheader("Results")

    st.write(
        f"Mean Reading = {mean_value:.6f}"
    )

    st.write(
        f"Standard Deviation = {std_dev:.6f}"
    )

    st.write(
        f"Repeatability Uncertainty = {u_repeat:.6f}"
    )

    st.write(
        f"Entered Temperature = {temperature:.1f} °C"
    )

    st.write(
        f"Temperature Difference = {delta_t:.2f} °C"
    )

    st.write(
        f"Dynamic Temperature Contribution = {dynamic_temp:.6f}"
    )

    st.write(
        f"Combined Uncertainty (Uc) = {uc:.6f}"
    )

    st.success(
        f"Expanded Uncertainty U(k=2) = ±{U:.6f}"
    )

    st.subheader("Reported Result")

    st.success(
        f"{mean_value:.6f} ± {U:.6f}"
    )
