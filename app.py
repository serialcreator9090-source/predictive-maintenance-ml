
import streamlit as st
import joblib
import pandas as pd

# Load the saved model
saved_data = joblib.load("predictive_maintenance_model.joblib")
model = saved_data["model"]
features = saved_data.get("features")

st.title("Predictive Maintenance Dashboard")
st.write("Enter machine sensor readings to predict failure risk.")

air_temp = st.number_input("Air temperature (K)", 290.0, 310.0, 300.0)
process_temp = st.number_input("Process temperature (K)", 300.0, 320.0, 310.0)
rotational_speed = st.number_input("Rotational speed (rpm)", 1000, 3000, 1500)
torque = st.number_input("Torque (Nm)", 0.0, 100.0, 40.0)
tool_wear = st.number_input("Tool wear (min)", 0, 250, 100)

if st.button("Predict machine failure"):
    input_data = pd.DataFrame([{
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": rotational_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }])

    if features is not None:
        input_data = input_data[features]

    prediction = model.predict(input_data)[0]

    st.write("Prediction:", "Failure detected" if prediction == 1 else "No failure predicted")

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0, 1]
        st.metric("Predicted failure risk", f"{probability:.1%}")
