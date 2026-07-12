# ⚡ AI-Powered Predictive Maintenance for Electrical Systems

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.6.1-F7931E?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

<img width="2720" height="880" alt="predictive_maintenance_banner" src="https://github.com/user-attachments/assets/5eaf7dd6-f679-4e78-a773-277fe4a7e983" />


An end-to-end Machine Learning pipeline and interactive Streamlit dashboard designed to predict imminent failures in electrical grids and industrial rotating machinery using telemetry data.

## 🚀 Project Overview
Predictive maintenance prevents costly downtime by identifying equipment anomalies before they lead to critical failures. This project simulates sensor telemetry (Voltage, Current, Temperature, Vibration) and utilizes a Random Forest classifier to flag physical stressors and alert operators in real-time.

**Key Features:**
* **Real-Time Monitoring:** Interactive UI built with Streamlit featuring a custom dark-mode design system.
* **Feature Engineering Pipeline:** Automated extraction of rolling averages, standard deviations, and lag variables to provide time-series context to the machine learning model.
* **Batch Diagnostics:** Upload CSV sensor logs to instantly detect critical failures and visualize temperature/vibration trends.
* **Synthetic Data Generation:** Custom Python scripts to generate robust, physics-based anomaly data for both grid transformers and industrial motors.
* **Interactive Visualizations:** Clean, dynamic charts highlighting anomaly points across time-series data.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (v1.6.1), Joblib
* **Visualization:** Matplotlib, Plotly
* **Frontend/UI:** Streamlit

## 💻 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/Nishit-soni-01/AI-Powered-Predictive-Maintenance-for-Electrical-Systems.git](https://github.com/Nishit-soni-01/AI-Powered-Predictive-Maintenance-for-Electrical-Systems.git)
cd AI-Powered-Predictive-Maintenance-for-Electrical-Systems
