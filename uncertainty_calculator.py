import streamlit as st
import pandas as pd

MASTER_BUDGET = {
    "Micrometer": {
        "0-25": {},
        "25-50": {},
        "50-75": {},
        "75-100": {}
    },

    "Caliper": {

        "0-150": {
            "Accuracy of Caliper Checker": {"value": 5.0, "distribution": "Rectangular", "dof": float("inf")},
            "Uncertainty of Caliper Checker": {"value": 3.8, "distribution": "Normal", "dof": float("inf")},
            "Accuracy of 5mm Master Ring": {"value": 1.1, "distribution": "Rectangular", "dof": float("inf")},
            "Uncertainty of 5mm Master Ring": {"value": 2.0, "distribution": "Normal", "dof": float("inf")},
            "Accuracy of 25mm Master Ring": {"value": 0.2, "distribution": "Rectangular", "dof": float("inf")},
            "Uncertainty of 25mm Master Ring": {"value": 1.0, "distribution": "Normal", "dof": float("inf")},
            "Accuracy of 10mm Pin": {"value": 0.5, "distribution": "Rectangular", "dof": float("inf")},
            "Uncertainty of 10mm Pin": {"value": 0.7, "distribution": "Normal", "dof": float("inf")},
            "Accuracy of Slip Gauge 25mm": {"value": 0.3, "distribution": "Rectangular", "dof": float("inf")},
            "Uncertainty of Slip Gauge 25mm": {"value": 0.1, "distribution": "Normal", "dof": float("inf")},
            "Resolution of Vernier": {"value": "dynamic", "distribution": "Rectangular", "dof": float("inf")}
        },

        "0-200": {},
        "0-300": {},
        "0-600": {}
    },


    "Plug Gauge": {
        "0.5-60": {},
        "60-200": {}
    },

    "Plunger Dial": {
        "0-1": {},
        "0-10": {}
    },

    "Dial Gauge": {
        "0-25": {}
    }
}

def get_budget(instrument, selected_range):
    return MASTER_BUDGET[instrument][selected_range]


st.title("NABL Uncertainty Calculator")

instrument = st.selectbox(
    "Select Instrument",
    list(MASTER_BUDGET.keys())
)

selected_range = st.selectbox(
    "Select Range",
    list(MASTER_BUDGET[instrument].keys())
)

budget = get_budget(instrument, selected_range)

st.write(budget)

L = st.number_input(
    "Measurement Size (mm)",
    min_value=0.0,
    value=10.0,
    step=0.01
)

st.write("Selected Size (L) =", L, "mm")

actual_temp = st.number_input(
    "Actual Temperature (°C)",
    value=20.0,
    step=0.1
)

st.write("Actual Temperature =", actual_temp, "°C")
TDEV = abs(actual_temp - 20)
st.write(
    "Temperature Deviation from 20°C =",
    round(TDEV, 3),
    "°C"
)

Taccuracy = 0.4
TUncertainty = 0.07
Tdiff = 0.2
alpha_avg = 0.0000081

st.write("Average CTE =", alpha_avg)


st.write("Temperature Accuracy =", Taccuracy)
st.write("Temperature Uncertainty =", TUncertainty)
st.write("Temperature Difference =", Tdiff)
u_temp_accuracy = Taccuracy * alpha_avg * L * 1000

st.write(
    "Temperature Sensor Accuracy Contribution (µm) =",
    round(u_temp_accuracy, 3)
)
u_temp_uncertainty = TUncertainty * alpha_avg * L * 1000

st.write(
    "Temperature Sensor Uncertainty Contribution (µm) =",
    round(u_temp_uncertainty, 3)
)

u_temp_difference = Tdiff * alpha_avg * L * 1000

st.write(
    "Temperature Difference Contribution (µm) =",
    round(u_temp_difference, 3)
)

u_ref_temperature = TDEV * alpha_avg * L * 1000

st.write(
    "Reference Temperature Contribution (µm) =",
    round(u_ref_temperature, 3)
)

st.subheader("Dynamic Temperature Contributors")
alpha_diff = 0.0000068

u_alpha_diff = alpha_diff * TDEV * L * 1000

st.write(
    "Coefficient of Expansion Contribution (µm) =",
    round(u_alpha_diff, 3)
)

budget_data = [
    ["Temperature Accuracy", u_temp_accuracy, "Rectangular", float("inf")],
    ["Temperature Uncertainty", u_temp_uncertainty, "Normal", float("inf")],
    ["Temperature Difference", u_temp_difference, "Rectangular", float("inf")],
    ["Reference Temperature", u_ref_temperature, "Rectangular", float("inf")],
    ["Coefficient of Expansion", u_alpha_diff, "Rectangular", float("inf")]
]
budget_df = pd.DataFrame(
    budget_data,
    columns=[
        "Contributor",
        "Value (µm)",
        "Distribution",
        "DOF"
    ]
)

st.subheader("Uncertainty Budget")

st.dataframe(
    budget_df,
    use_container_width=True
)

standard_uncertainties = []

for item in budget_data:

    contributor = item[0]
    value = item[1]
    distribution = item[2]
    dof = item[3]

    if distribution == "Rectangular":
        std_unc = value / (3 ** 0.5)

    elif distribution == "Normal":
        std_unc = value

    else:
        std_unc = value

    standard_uncertainties.append(
        [contributor, value, distribution, std_unc, dof]
    )

budget_std_df = pd.DataFrame(
    standard_uncertainties,
    columns=[
        "Contributor",
        "Value (µm)",
        "Distribution",
        "Std Uncertainty (µm)",
        "DOF"
    ]
)

st.subheader("Standard Uncertainty Budget")

st.dataframe(
    budget_std_df,
    use_container_width=True
)



#st.write(budget)

#st.success(f"Selected Instrument : {instrument}")
#st.success(f"Selected Range : {selected_range}")
