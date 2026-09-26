import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import t


MASTER_BUDGET = {

    "Micrometer": {

        "0-25": {
            "Accuracy of Slip Gauges": {
                "value": 0.300,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Slip Gauge from Certificate": {
                "value": 0.251,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Resolution of Micrometer": {
                "value": 1.0,
                "distribution": "Rectangular",
                "dof": float("inf")
            }
        },

        "25-50": {
            "Accuracy of Slip Gauges": {
                "value": 0.300,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Slip Gauge from Certificate": {
                "value": 0.251,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Resolution of Micrometer": {
                "value": 1.0,
                "distribution": "Rectangular",
                "dof": float("inf")
            }
        },

        "50-75": {
            "Accuracy of Slip Gauges": {
                "value": 0.300,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Slip Gauge from Certificate": {
                "value": 0.251,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Resolution of Micrometer": {
                "value": 1.0,
                "distribution": "Rectangular",
                "dof": float("inf")
            }
        },

        "75-100": {
            "Accuracy of Slip Gauges": {
                "value": 0.300,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Slip Gauge from Certificate": {
                "value": 0.251,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Resolution of Micrometer": {
                "value": 1.0,
                "distribution": "Rectangular",
                "dof": float("inf")
            }
        }
    },

    "Caliper": {

        "0-150": {
            "Accuracy of Caliper Checker": {
                "value": 5.0,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Caliper Checker": {
                "value": 3.8,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Accuracy of 5mm Master Ring": {
                "value": 1.1,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of 5mm Master Ring": {
                "value": 2.0,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Accuracy of 25mm Master Ring": {
                "value": 0.2,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of 25mm Master Ring": {
                "value": 1.0,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Accuracy of 10mm Pin": {
                "value": 0.5,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of 10mm Pin": {
                "value": 0.7,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Accuracy of Slip Gauge 25mm": {
                "value": 0.3,
                "distribution": "Rectangular",
                "dof": float("inf")
            },
            "Uncertainty of Slip Gauge 25mm": {
                "value": 0.1,
                "distribution": "Normal",
                "dof": float("inf")
            },
            "Resolution of Vernier": {
                "value": "dynamic",
                "distribution": "Rectangular",
                "dof": float("inf")
            }
        },

        "0-200": {},
        "0-300": {},
        "0-600": {}
    },

    "Plain Plug Gauge": {

    "0.5-60": {

        "Accuracy of Equipment": {
            "value": 0.5,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Equipment Calibration": {
            "value": 0.5,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Accuracy of Slip Gauge": {
            "value": 0.4242640687,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Slip Gauge": {
            "value": 0.1838477631,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Resolution of Comparator": {
            "value": 0.1,
            "distribution": "Rectangular",
            "dof": float("inf")
        }
    },

    "60-200": {

        "Accuracy of Equipment": {
            "value": 0.5,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Equipment Calibration": {
            "value": 0.5,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Accuracy of Slip Gauge": {
            "value": 0.4242640687,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Slip Gauge": {
            "value": 0.1838477631,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Resolution of Comparator": {
            "value": 0.1,
            "distribution": "Rectangular",
            "dof": float("inf")
        }
    }
},
"Analog Dial": {

    "0-1": {

        "Accuracy of Equipment (DCT)": {
            "value": "dynamic_dct",
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Equipment Calibration (DCT)": {
            "value": 0.400,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Resolution of Equipment (DCT)": {
            "value": 0.1,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Resolution of Dial Gauge": {
            "value": 1.0,
            "distribution": "Rectangular",
            "dof": float("inf")
        }
    },

    "0-10": {

        "Accuracy of Equipment (DCT)": {
            "value": "dynamic_dct",
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Equipment Calibration (DCT)": {
            "value": 0.400,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Resolution of Equipment (DCT)": {
            "value": 0.1,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Resolution of Dial Gauge": {
            "value": 1.0,
            "distribution": "Rectangular",
            "dof": float("inf")
        }
    }
},

"Digital Dial": {

    "0-25": {

        "Accuracy of Equipment (ULM)": {
            "value": "dynamic_ulm",
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Uncertainty of Equipment Calibration (ULM)": {
            "value": 0.900,
            "distribution": "Normal",
            "dof": float("inf")
        },

        "Resolution of Equipment (ULM)": {
            "value": 0.1,
            "distribution": "Rectangular",
            "dof": float("inf")
        },

        "Resolution of Dial Gauge": {
            "value": 1.0,
            "distribution": "Rectangular",
            "dof": float("inf")
        }
    }
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


INSTRUMENT_CONSTANTS = {

    "Micrometer": {
        "alpha_avg": 0.0000081,
        "alpha_diff": 0.0000068,
        "Taccuracy": 0.4,
        "TUncertainty": 0.07,
        "Tdiff": 0.2
    },

    "Caliper": {
        "alpha_avg": 0.0000115,
        "alpha_diff": 0.0000115,
        "Taccuracy": 0.4,
        "TUncertainty": 0.07,
        "Tdiff": 0.2
    },

    "Plain Plug Gauge": {
        "alpha_avg": 0.0000098,
        "alpha_diff": 0.0000034,
        "Taccuracy": 0.4,
        "TUncertainty": 0.07,
        "Tdiff": 0.2
    },

    "Analog Dial": {
        "alpha_avg": 0.0000115,
        "alpha_diff": 0.0000115,
        "Taccuracy": 0.4,
        "TUncertainty": 0.07,
        "Tdiff": 0.2
    },

    "Digital Dial": {
        "alpha_avg": 0.0000115,
        "alpha_diff": 0.0000115,
        "Taccuracy": 0.4,
        "TUncertainty": 0.08,
        "Tdiff": 0.2
    }
}

constants = INSTRUMENT_CONSTANTS[instrument]

alpha_avg = constants["alpha_avg"]
alpha_diff = constants["alpha_diff"]

Taccuracy = constants["Taccuracy"]
TUncertainty = constants["TUncertainty"]
Tdiff = constants["Tdiff"]


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


st.subheader("Repeatability Readings")

r1 = st.number_input(
    "Reading 1",
    value=0.0000,
    step=0.0001,
    format="%.4f"
)

r2 = st.number_input(
    "Reading 2",
    value=0.0000,
    step=0.0001,
    format="%.4f"
)

r3 = st.number_input(
    "Reading 3",
    value=0.0000,
    step=0.0001,
    format="%.4f"
)

r4 = st.number_input(
    "Reading 4",
    value=0.0000,
    step=0.0001,
    format="%.4f"
)

r5 = st.number_input(
    "Reading 5",
    value=0.0000,
    step=0.0001,
    format="%.4f"
)



st.subheader("Repeatability Results")

readings = [r1, r2, r3, r4, r5]

mean_reading = np.mean(readings)

std_dev = np.std(readings, ddof=1)

u_repeatability = std_dev / np.sqrt(len(readings))

st.write("Mean =", round(mean_reading, 4))
st.write("Standard Deviation =", round(std_dev, 4))
st.write("Repeatability Uncertainty =", round(u_repeatability, 4))


budget_data = []

budget_data.append(
    ["Repeatability", u_repeatability, "Normal", 4]
)

budget_data.append(
    ["Temperature Accuracy", u_temp_accuracy, "Rectangular", float("inf")]
)

budget_data.append(
    ["Temperature Uncertainty", u_temp_uncertainty, "Normal", float("inf")]
)

budget_data.append(
    ["Temperature Difference", u_temp_difference, "Rectangular", float("inf")]
)

budget_data.append(
    ["Reference Temperature", u_ref_temperature, "Rectangular", float("inf")]
)

budget_data.append(
    ["Coefficient of Expansion", u_alpha_diff, "Rectangular", float("inf")]
)

for contributor, details in budget.items():

    value = details["value"]

    if value == "dynamic_dct":
        value = 0.8 + (0.2 * L)

    elif value == "dynamic_ulm":
        value = 0.5 + (L / 1000)

    distribution = details["distribution"]

    dof = details["dof"]

    budget_data.append(
        [contributor, value, distribution, dof]
    )



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

    if not isinstance(value, (int, float)):
        continue
    distribution = item[2]
    dof = item[3]

    if distribution == "Rectangular":
        std_unc = value / (3 ** 0.5)

    elif distribution == "Normal":
        std_unc = value

    else:
        std_unc = value


    ci = 1

    standard_uncertainties.append(
        [
            contributor,
            value,
            distribution,
            ci,
            std_unc,
            dof
        ]
    )




budget_std_df = pd.DataFrame(
    standard_uncertainties,
    columns=[
        "Contributor",
        "Value (µm)",
        "Distribution",
        "Ci",
        "Std Uncertainty (µm)",
        "DOF"
    ]
)


st.subheader("Standard Uncertainty Budget")

st.dataframe(
    budget_std_df,
    use_container_width=True
)


Uc = np.sqrt(
    np.sum(
        budget_std_df["Std Uncertainty (µm)"] ** 2
    )
)

st.subheader("Combined Standard Uncertainty")



st.write(
    f"Combined Standard Uncertainty (Uc) = {Uc:.4f} µm"
)

st.write(
    f"Effective Degrees of Freedom (Veff) = {veff:.2f}"
)

veff_denominator = 0

for _, _, _, _, std_unc, dof in standard_uncertainties:

    if dof != float("inf") and std_unc > 0:
        veff_denominator += (std_unc ** 4) / dof

if veff_denominator > 0:
    veff = (Uc ** 4) / veff_denominator
else:
    veff = float("inf")

st.subheader("Effective Degrees of Freedom (Veff)")

if veff == float("inf"):
    st.write("∞")
else:
    st.write(round(veff, 2))



if veff == float("inf"):
    k = 2
else:
    k = t.ppf(0.975, veff)

st.subheader("Coverage Factor (k)")
st.write(round(k, 4))


expanded_uncertainty = Uc * k




st.subheader("Expanded Uncertainty")

st.write(
    round(expanded_uncertainty, 4),
    "µm"
)


#st.write(budget)

#st.success(f"Selected Instrument : {instrument}")
#st.success(f"Selected Range : {selected_range}")
