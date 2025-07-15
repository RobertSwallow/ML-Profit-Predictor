import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model_with_states.pkl")

st.title("Startup Profit Predictor")

# Input fields
r_and_d = st.number_input("R&D Spend", min_value=0.0, step=1000.0)
admin = st.number_input("Administration Spend", min_value=0.0, step=1000.0)
marketing = st.number_input("Marketing Spend", min_value=0.0, step=1000.0)

state = st.radio("State", ("California", "Florida", "New York", "Other"))

# One-hot encode state
state_input = [0, 0, 0]
if state == "California":
    state_input[0] = 1
elif state == "Florida":
    state_input[1] = 1
elif state == "New York":
    state_input[2] = 1

if st.button("Predict Profit"):
    if admin < 50000:
        st.error("Administration Spend must be at least $50,000 for a reliable prediction.")
    elif admin > 400000 or r_and_d > 400000 or marketing > 400000:
        st.error("R&D Spend, Administration Spend, and Marketing Spend must each be under $400,000 for a reliable prediction.")
    else:
        features = np.array([[r_and_d, admin, marketing] + state_input])
        prediction = model.predict(features)[0]
        st.success(f"Predicted Profit: ${prediction:,.2f}")

        total_investment = r_and_d + admin + marketing
        roi = (prediction / total_investment) * 100 if total_investment > 0 else 0

        st.write(f"Total Investment: ${total_investment:,.2f}")
        st.write(f"Predicted ROI: {roi:.2f}%")

        if roi < 20:
            st.warning("ROI is below target investment threshold.")
        else:
            st.success("ROI meets investment expectations!")
