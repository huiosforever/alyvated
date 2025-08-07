# pages/02_Safety_Monitoring.py
# Biometric thresholds + CV gait/slip risk. Auto-mitigation.
# Covers: vitals, gait analysis, emergency protocol [oai_citation:14‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:15‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import safety, devices

st.title("Safety Monitoring & AI Risk Mitigation")

cfg = safety.load_thresholds()
st.sidebar.header("Thresholds")
cfg.hr_min = st.sidebar.slider("Min HR (bpm)", 30, 60, cfg.hr_min)
cfg.spo2_min = st.sidebar.slider("Min SpO₂ (%)", 80, 98, cfg.spo2_min)
cfg.motion_timeout_s = st.sidebar.slider("Motion Timeout (s)", 5, 30, cfg.motion_timeout_s)
safety.save_thresholds(cfg)

st.subheader("Simulate Incoming Signals")
col1, col2, col3 = st.columns(3)
hr = col1.slider("Heart Rate (bpm)", 30, 180, 54)
spo2 = col2.slider("SpO₂ (%)", 75, 100, 92)
motion = col3.toggle("Motion Detected", value=True)

gait_risk = st.selectbox("Pre-Entry Gait Risk", ["Low", "Medium", "High"])

alerts = safety.evaluate_inputs(hr, spo2, motion, gait_risk)
if alerts.trigger_emergency:
    st.error("EMERGENCY: Drain + Temp Mitigation triggered.")
    devices.emergency_drain(st.session_state.system)
elif alerts.restrict_depth:
    st.warning("Gait risk detected → preemptively reducing depth.")
    devices.reduce_depth(st.session_state.system)
else:
    st.success("Within safe envelope.")

st.json(alerts.__dict__)
