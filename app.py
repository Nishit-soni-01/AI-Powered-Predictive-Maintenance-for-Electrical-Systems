import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configuration
st.set_page_config(page_title="Electrical System Maintenance AI", layout="wide")

# Load Model and Feature List
@st.cache_resource
def load_model():
    model = joblib.load('rf_maintenance_model.pkl')
    features = joblib.load('model_features.pkl')
    return model, features

model, features = load_model()

st.title("⚡ AI-Powered Predictive Maintenance for Electrical Systems")
st.markdown("Upload a CSV of recent sensor logs to predict if a system failure is imminent in the next 24 hours.")

# Sidebar for manual single-entry testing
st.sidebar.header("Live Sensor Input")
voltage = st.sidebar.slider("Voltage (V)", 200.0, 250.0, 230.0)
current = st.sidebar.slider("Current (A)", 5.0, 20.0, 10.0)
temperature = st.sidebar.slider("Temperature (°C)", 20.0, 80.0, 45.0)
vibration = st.sidebar.slider("Vibration (mm/s)", 0.0, 5.0, 2.0)

# Main panel for Batch Processing
uploaded_file = st.file_uploader("Upload Sensor Log (CSV format)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Raw Sensor Data")
    st.write(data.tail())
    
    # Check if data has required features
    missing_cols = [col for col in features if col not in data.columns]
    
    if len(missing_cols) > 0:
        st.error(f"Missing required columns from feature engineering: {missing_cols}")
        st.info("Ensure your CSV includes rolling averages and lag features.")
    else:
        if st.button("Run Diagnostics"):
            predictions = model.predict(data[features])
            data['Failure_Prediction'] = predictions
            
            # Display Results
            alerts = data[data['Failure_Prediction'] == 1]
            if len(alerts) > 0:
                st.error(f"⚠️ WARNING: {len(alerts)} instances of imminent failure detected in the logs!")
                st.dataframe(alerts)
            else:
                st.success("✅ System operating within normal parameters. No failures predicted.")