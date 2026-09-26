import streamlit as st

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



#st.write(budget)

#st.success(f"Selected Instrument : {instrument}")
#st.success(f"Selected Range : {selected_range}")
