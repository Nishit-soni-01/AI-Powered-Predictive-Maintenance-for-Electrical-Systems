# ⚡ AI-Powered Predictive Maintenance for Electrical Systems


**🌐 Live Web App:** [Click here to launch the Predictive Maintenance AI](https://your-app-name.streamlit.app/)

**Author:** Nishit Soni  
**Institution:** ABES Engineering College, Ghaziabad, Uttar Pradesh  
**Role:** AI Engineer / Data Scientist  

## 📌 Project Overview
This project bridges the gap between core electrical engineering domains and advanced machine learning. It features a Random Forest Classifier trained on multivariate time-series sensor data (Voltage, Current, Temperature, Vibration) to predict equipment failure up to 24 hours before it occurs. 

By identifying anomalies early, this system is designed to facilitate proactive maintenance, potentially reducing unplanned equipment downtime by up to 30%.

## 🛠️ Tech Stack & Skills Showcased
* **Languages:** Python (Pandas, NumPy)
* **Machine Learning:** Scikit-Learn (Random Forest, Hyperparameter tuning)
* **Feature Engineering:** Time-series manipulation, rolling window statistics, lag features.
* **Deployment:** Streamlit, Joblib

## 🧠 Advanced Feature Engineering 
Instead of relying solely on raw sensor inputs, this model utilizes calculated time-series metrics to capture system stress over time:
- **Rolling Means:** `temp_roll_mean_6h`, `vib_roll_mean_6h` (Smoothing noise)
- **Rolling Standard Deviations:** `current_roll_std_12h`, `vib_roll_std_12h` (Capturing operational volatility and frequency-domain proxies)
- **Lag Variables:** Capturing immediate historical state changes.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/predictive-maintenance-ai.git](https://github.com/yourusername/predictive-maintenance-ai.git)
   cd predictive-maintenance-ai
