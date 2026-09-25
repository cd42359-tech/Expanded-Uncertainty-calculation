import streamlit as st

MASTER_BUDGET = {
    "Micrometer": {
        "0-25": {},
        "25-50": {},
        "50-75": {},
        "75-100": {}
    },

    "Caliper": {
        "0-150": {},
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

st.success(f"Selected Instrument : {instrument}")
st.success(f"Selected Range : {selected_range}")
