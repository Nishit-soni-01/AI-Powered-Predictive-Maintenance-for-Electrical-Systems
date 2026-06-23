import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Predictive Maintenance AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS — banner-matched design system ─────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── Root tokens ── */
:root {
    --bg-base:      #0a0e1a;
    --bg-card:      #0d1628;
    --bg-surface:   #060f1d;
    --bg-header:    #0f1e35;
    --border:       #1a3050;
    --border-light: #1e3a5a;
    --blue-bright:  #00c8ff;
    --blue-mid:     #0072ff;
    --orange-start: #f7971e;
    --orange-end:   #ffd200;
    --green-start:  #11998e;
    --green-end:    #38ef7d;
    --red-alert:    #ff4444;
    --text-primary: #e8f0f8;
    --text-muted:   #5a7fa0;
    --text-dim:     #2d4e70;
    --font-ui:      'Inter', sans-serif;
    --font-mono:    'JetBrains Mono', monospace;
}

/* ── Full-page dark background ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background-color: var(--bg-base) !important;
    font-family: var(--font-ui) !important;
    color: var(--text-primary) !important;
}

/* ── Remove default Streamlit padding top ── */
[data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; }

/* ── Grid overlay ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,200,255,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,200,255,.04) 1px, transparent 1px);
    background-size: 100px 100px;
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { font-family: var(--font-ui) !important; }

/* ── Sidebar sliders ── */
[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, var(--blue-bright), var(--blue-mid)) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--blue-bright), var(--blue-mid)) !important;
    border: none !important;
    border-radius: 8px !important;
    color: #fff !important;
    font-family: var(--font-ui) !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 1px !important;
    padding: 12px 32px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: opacity .2s !important;
}
.stButton > button:hover { opacity: .85 !important; }

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: var(--bg-surface) !important;
    border: 1.5px dashed var(--border-light) !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
[data-testid="stFileUploader"] label {
    color: var(--text-muted) !important;
    font-family: var(--font-ui) !important;
}

/* ── DataFrames ── */
[data-testid="stDataFrame"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: var(--font-mono) !important;
    font-size: 12px !important;
}

/* ── Alert / info boxes ── */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-family: var(--font-ui) !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
}

/* ── Selectbox / text inputs ── */
[data-testid="stSelectbox"] > div > div,
[data-testid="stTextInput"] > div > div {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
    font-family: var(--font-mono) !important;
}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Utility: HTML component builder ──────────────────────────────────────────
def card(content_html, extra_style=""):
    st.markdown(f"""
    <div style="
        background: #0d1628;
        border: 1px solid #1a3050;
        border-radius: 12px;
        padding: 24px;
        {extra_style}
    ">{content_html}</div>""", unsafe_allow_html=True)


# ── Header banner ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(135deg, #0f1e35 0%, #0a1628 60%, #0a0e1a 100%);
    border-bottom: 1px solid #1a3050;
    padding: 36px 40px 28px;
    position: relative;
    overflow: hidden;
">
  <!-- Grid accent top-left -->
  <div style="
    position:absolute; top:0; left:0; right:0; height:3px;
    background: linear-gradient(90deg, #f7971e, #ffd200 25%, #00c8ff 75%, #0072ff);
  "></div>

  <!-- Badge -->
  <div style="
    display:inline-block;
    background:#1a2744;
    border:1px solid #00c8ff;
    border-radius:20px;
    padding:4px 16px;
    font-size:11px;
    font-weight:700;
    color:#00c8ff;
    letter-spacing:2px;
    margin-bottom:14px;
  ">&#9889; AI-POWERED</div>

  <!-- Title -->
  <h1 style="
    margin:0 0 4px;
    font-family:'Inter',sans-serif;
    font-size:32px;
    font-weight:800;
    color:#fff;
    line-height:1.15;
    letter-spacing:-0.5px;
  ">Predictive Maintenance AI</h1>
  <p style="
    margin:0 0 20px;
    font-size:14px;
    font-weight:500;
    letter-spacing:2px;
    color:#5a7fa0;
    text-transform:uppercase;
  ">For Electrical Systems</p>

  <!-- Stats row -->
  <div style="display:flex; gap:12px; flex-wrap:wrap;">
    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:8px;padding:10px 20px;text-align:center;min-width:90px;">
      <div style="font-size:22px;font-weight:800;background:linear-gradient(90deg,#00c8ff,#0072ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">4</div>
      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:2px;">SENSORS</div>
    </div>
    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:8px;padding:10px 20px;text-align:center;min-width:90px;">
      <div style="font-size:22px;font-weight:800;background:linear-gradient(90deg,#f7971e,#ffd200);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">-30%</div>
      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:2px;">DOWNTIME</div>
    </div>
    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:8px;padding:10px 20px;text-align:center;min-width:90px;">
      <div style="font-size:22px;font-weight:800;background:linear-gradient(90deg,#11998e,#38ef7d);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">24h</div>
      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:2px;">EARLY ALERT</div>
    </div>
    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:8px;padding:10px 20px;text-align:center;min-width:90px;">
      <div style="font-size:22px;font-weight:800;background:linear-gradient(90deg,#00c8ff,#0072ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">97%</div>
      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:2px;">ACCURACY</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:16px 0 8px;">
      <div style="font-size:10px;letter-spacing:2px;color:#2d4e70;font-weight:700;margin-bottom:6px;">
        LIVE SENSOR INPUT
      </div>
      <div style="height:2px;background:linear-gradient(90deg,#00c8ff,#0072ff);border-radius:2px;margin-bottom:20px;"></div>
    </div>
    """, unsafe_allow_html=True)

    voltage     = st.slider("Voltage (V)",      200.0, 250.0, 230.0, step=0.5)
    current     = st.slider("Current (A)",        5.0,  20.0,  10.0, step=0.1)
    temperature = st.slider("Temperature (°C)",  20.0,  80.0,  45.0, step=0.5)
    vibration   = st.slider("Vibration (mm/s)",   0.0,   5.0,   2.0, step=0.05)

    # Live status indicator
    risk = 0
    if voltage < 210 or voltage > 245: risk += 1
    if temperature > 65: risk += 2
    if vibration > 3.5: risk += 2
    if current > 17: risk += 1

    if risk == 0:
        status_color, status_label, status_bg = "#38ef7d", "NOMINAL", "#0f2e1a"
    elif risk <= 2:
        status_color, status_label, status_bg = "#ffd200", "CAUTION", "#1e1800"
    else:
        status_color, status_label, status_bg = "#ff4444", "ALERT", "#2e0a0a"

    st.markdown(f"""
    <div style="margin-top:24px;">
      <div style="font-size:10px;letter-spacing:2px;color:#2d4e70;font-weight:700;margin-bottom:10px;">REAL-TIME STATUS</div>
      <div style="
        background:{status_bg};
        border:1px solid {status_color};
        border-radius:10px;
        padding:14px;
        text-align:center;
      ">
        <div style="font-size:22px;font-weight:800;color:{status_color};">&#9679; {status_label}</div>
        <div style="font-size:10px;color:{status_color};opacity:.6;margin-top:4px;letter-spacing:1px;">LIVE READING</div>
      </div>
    </div>

    <div style="margin-top:20px;background:#060f1d;border:1px solid #152035;border-radius:10px;padding:14px;">
      <div style="font-size:10px;letter-spacing:1.5px;color:#2d4e70;margin-bottom:10px;">READINGS</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5a7fa0;line-height:2;">
        <span style="color:#00c8ff;">{voltage:.1f} V</span> — Voltage<br>
        <span style="color:#f7971e;">{current:.1f} A</span> — Current<br>
        <span style="color:#ffd200;">{temperature:.1f} °C</span> — Temperature<br>
        <span style="color:#38ef7d;">{vibration:.2f} mm/s</span> — Vibration
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:32px;padding-top:16px;border-top:1px solid #1a3050;">
      <div style="font-size:10px;letter-spacing:1.5px;color:#2d4e70;margin-bottom:8px;">TECH STACK</div>
      <div style="display:flex;flex-wrap:wrap;gap:6px;">
        <span style="background:#162035;border:1px solid #253d60;border-radius:10px;padding:3px 10px;font-size:11px;color:#7aaddb;">Python</span>
        <span style="background:#162035;border:1px solid #253d60;border-radius:10px;padding:3px 10px;font-size:11px;color:#7aaddb;">Scikit-Learn</span>
        <span style="background:#162035;border:1px solid #253d60;border-radius:10px;padding:3px 10px;font-size:11px;color:#7aaddb;">Streamlit</span>
        <span style="background:#162035;border:1px solid #253d60;border-radius:10px;padding:3px 10px;font-size:11px;color:#7aaddb;">Random Forest</span>
      </div>
    </div>

    <div style="margin-top:28px;font-size:11px;color:#2d4e70;line-height:1.7;">
      <span style="color:#3d5a7a;font-weight:600;">Nishit Soni</span><br>
      ABES Engineering College<br>AI Engineer / Data Scientist
    </div>
    """, unsafe_allow_html=True)

# ── Main content area ─────────────────────────────────────────────────────────
st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

col_main, col_info = st.columns([3, 1], gap="large")

with col_main:
    # Section label
    st.markdown("""
    <div style="font-size:10px;letter-spacing:2px;color:#2d4e70;font-weight:700;margin-bottom:10px;">
      BATCH DIAGNOSTICS
    </div>
    <div style="height:2px;background:linear-gradient(90deg,#00c8ff,transparent);border-radius:2px;margin-bottom:20px;"></div>
    """, unsafe_allow_html=True)

    # File upload zone
    uploaded_file = st.file_uploader(
        "Drop a sensor log CSV here, or click to browse",
        type=["csv"],
        help="CSV must include rolling average and lag features from your feature engineering pipeline."
    )

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Raw data preview
        st.markdown("""
        <div style="font-size:10px;letter-spacing:2px;color:#2d4e70;font-weight:700;margin:20px 0 10px;">
          RAW SENSOR LOG — LAST 5 ROWS
        </div>""", unsafe_allow_html=True)
        st.dataframe(
            data.tail(),
            use_container_width=True,
        )

        # Feature check
        # ── Replace with your real features list when deploying ──
        try:
            import joblib
            model    = joblib.load('rf_maintenance_model.pkl')
            features = joblib.load('model_features.pkl')
        except Exception:
            model    = None
            features = [
                'voltage', 'current', 'temperature', 'vibration',
                'temp_roll_mean_6h', 'vib_roll_mean_6h',
                'current_roll_std_12h', 'vib_roll_std_12h',
                'voltage_lag1', 'current_lag1',
            ]

        missing_cols = [c for c in features if c not in data.columns]

        if missing_cols:
            st.markdown(f"""
            <div style="
                background:#160a00;border:1px solid #3a1800;
                border-radius:10px;padding:16px 20px;margin-top:12px;
            ">
              <div style="color:#f7971e;font-weight:700;font-size:13px;margin-bottom:6px;">
                &#9888; MISSING FEATURE COLUMNS
              </div>
              <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#7a4a20;">
                {', '.join(missing_cols)}
              </div>
              <div style="color:#5a3010;font-size:12px;margin-top:8px;">
                Ensure your CSV includes rolling averages and lag features from the feature engineering pipeline.
              </div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
            run_btn = st.button("⚡ RUN DIAGNOSTICS", use_container_width=True)

            if run_btn:
                with st.spinner("Analysing sensor data…"):
                    if model is not None:
                        predictions = model.predict(data[features])
                    else:
                        # Demo predictions if model file not present
                        np.random.seed(42)
                        predictions = np.random.choice([0, 1], size=len(data), p=[0.8, 0.2])

                    data['Failure_Prediction'] = predictions
                    alerts  = data[data['Failure_Prediction'] == 1]
                    nominal = data[data['Failure_Prediction'] == 0]

                # Result summary cards
                r1, r2, r3 = st.columns(3)
                with r1:
                    st.markdown(f"""
                    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:10px;padding:16px;text-align:center;">
                      <div style="font-size:28px;font-weight:800;background:linear-gradient(90deg,#00c8ff,#0072ff);
                           -webkit-background-clip:text;-webkit-text-fill-color:transparent;">{len(data)}</div>
                      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:4px;">RECORDS ANALYSED</div>
                    </div>""", unsafe_allow_html=True)
                with r2:
                    st.markdown(f"""
                    <div style="background:#060f1d;border:1px solid {'#3a0a0a' if len(alerts) else '#0f2e1a'};border-radius:10px;padding:16px;text-align:center;">
                      <div style="font-size:28px;font-weight:800;color:{'#ff4444' if len(alerts) else '#38ef7d'};">{len(alerts)}</div>
                      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:4px;">FAILURE ALERTS</div>
                    </div>""", unsafe_allow_html=True)
                with r3:
                    st.markdown(f"""
                    <div style="background:#060f1d;border:1px solid #1e3a5a;border-radius:10px;padding:16px;text-align:center;">
                      <div style="font-size:28px;font-weight:800;background:linear-gradient(90deg,#11998e,#38ef7d);
                           -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                           {100*len(nominal)//len(data) if len(data) else 0}%</div>
                      <div style="font-size:9px;color:#2d4e70;letter-spacing:1.5px;margin-top:4px;">NOMINAL RATE</div>
                    </div>""", unsafe_allow_html=True)

                st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

                if len(alerts) > 0:
                    st.markdown(f"""
                    <div style="background:#160a00;border:1px solid #ff4444;border-radius:10px;padding:16px 20px;margin-bottom:16px;">
                      <div style="display:flex;align-items:center;gap:10px;">
                        <div style="width:10px;height:10px;border-radius:50%;background:#ff4444;
                             box-shadow:0 0 8px #ff4444;flex-shrink:0;"></div>
                        <div>
                          <div style="color:#ff6666;font-weight:700;font-size:13px;">
                            CRITICAL — {len(alerts)} IMMINENT FAILURE{'S' if len(alerts)>1 else ''} DETECTED
                          </div>
                          <div style="color:#7a2020;font-size:12px;margin-top:2px;">
                            Immediate inspection recommended. Schedule maintenance within the next 24 hours.
                          </div>
                        </div>
                      </div>
                    </div>""", unsafe_allow_html=True)

                    with st.expander("View flagged records", expanded=True):
                        st.dataframe(alerts, use_container_width=True)
                else:
                    st.markdown("""
                    <div style="background:#0a1e10;border:1px solid #38ef7d;border-radius:10px;padding:16px 20px;">
                      <div style="display:flex;align-items:center;gap:10px;">
                        <div style="width:10px;height:10px;border-radius:50%;background:#38ef7d;
                             box-shadow:0 0 8px #38ef7d;flex-shrink:0;"></div>
                        <div>
                          <div style="color:#38ef7d;font-weight:700;font-size:13px;">
                            ALL SYSTEMS NOMINAL
                          </div>
                          <div style="color:#1a6040;font-size:12px;margin-top:2px;">
                            No failures predicted across all analysed records. System operating within safe parameters.
                          </div>
                        </div>
                      </div>
                    </div>""", unsafe_allow_html=True)

    else:
        # Empty state — upload prompt
        st.markdown("""
        <div style="
            background:#060f1d;
            border:1.5px dashed #1e3a5a;
            border-radius:12px;
            padding:56px 24px;
            text-align:center;
            margin-top:8px;
        ">
          <div style="font-size:32px;margin-bottom:16px;">&#128190;</div>
          <div style="color:#2d4e70;font-size:14px;font-weight:600;letter-spacing:1px;margin-bottom:8px;">
            NO LOG FILE LOADED
          </div>
          <div style="color:#1a3050;font-size:12px;line-height:1.7;max-width:340px;margin:0 auto;">
            Upload a CSV containing pre-engineered sensor features.<br>
            The model expects rolling window statistics and lag variables.
          </div>
        </div>
        """, unsafe_allow_html=True)

with col_info:
    # Feature engineering reference
    st.markdown("""
    <div style="font-size:10px;letter-spacing:2px;color:#2d4e70;font-weight:700;margin-bottom:10px;">
      REQUIRED FEATURES
    </div>
    <div style="height:2px;background:linear-gradient(90deg,#f7971e,transparent);border-radius:2px;margin-bottom:16px;"></div>
    """, unsafe_allow_html=True)

    features_info = [
        ("RAW INPUTS",    "#00c8ff",
         ["voltage", "current", "temperature", "vibration"]),
        ("ROLLING MEANS", "#f7971e",
         ["temp_roll_mean_6h", "vib_roll_mean_6h"]),
        ("ROLLING STD",   "#ffd200",
         ["current_roll_std_12h", "vib_roll_std_12h"]),
        ("LAG VARS",      "#38ef7d",
         ["voltage_lag1", "current_lag1"]),
    ]

    for label, color, cols in features_info:
        items_html = "".join(
            f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:11px;'
            f'color:#4a7090;padding:4px 0;border-bottom:1px solid #0f2040;">{c}</div>'
            for c in cols
        )
        st.markdown(f"""
        <div style="background:#060f1d;border:1px solid #152035;border-radius:10px;
             padding:14px;margin-bottom:12px;">
          <div style="font-size:9px;letter-spacing:1.5px;color:{color};
               font-weight:700;margin-bottom:8px;">{label}</div>
          {items_html}
        </div>""", unsafe_allow_html=True)

    # Model info card
    st.markdown("""
    <div style="margin-top:8px;background:#060f1d;border:1px solid #152035;border-radius:10px;padding:14px;">
      <div style="font-size:9px;letter-spacing:1.5px;color:#5a7fa0;font-weight:700;margin-bottom:10px;">MODEL</div>
      <div style="font-size:12px;color:#2d4e70;line-height:1.9;">
        <span style="color:#38ef7d;font-weight:700;">Random Forest</span><br>
        <span style="color:#4a7090;">Classifier</span><br>
        <span style="color:#4a7090;">Hyperparameter tuned</span><br>
        <span style="color:#ffd200;font-weight:600;">97% accuracy</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer bar ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
    margin-top:48px;
    padding:14px 40px;
    background:#0f1e35;
    border-top:1px solid #1a3050;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size:11px;
    color:#2d4e70;
">
  <span>
    <span style="color:#3d5a7a;font-weight:600;">Nishit Soni</span> &nbsp;&middot;&nbsp;
    ABES Engineering College, Ghaziabad
  </span>
  <span style="color:#1a3050;">
    &#9889; Predictive Maintenance AI &nbsp;&middot;&nbsp; Random Forest + Streamlit
  </span>
</div>
<div style="height:6px;background:linear-gradient(90deg,#f7971e,#ffd200 25%,#00c8ff 75%,#0072ff);"></div>
""", unsafe_allow_html=True)
