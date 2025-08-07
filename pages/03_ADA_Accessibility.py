# pages/03_ADA_Accessibility.py
# ADA lift & ramp memory, gesture controls [oai_citation:16‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import ada

st.title("ADA Access & Gesture Control")

profile = ada.get_profile()
col1, col2 = st.columns(2)
with col1:
    depth = st.slider("Seat Depth (cm)", 20, 80, profile.seat_depth_cm)
    angle = st.slider("Ramp Angle (°)", 0, 20, profile.ramp_angle_deg)
    fail_safe = st.toggle("Battery Fail‑Safe", value=True)
with col2:
    use_gestures = st.toggle("Enable Gesture/Sign Controls", value=True)  # hands-free [oai_citation:17‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
    auto_level   = st.toggle("Auto-Level Ramp", value=True)

if st.button("Save ADA Profile"):
    ada.save_profile(depth, angle, fail_safe, use_gestures, auto_level)
    st.success("Saved.")

st.info("Try gestures on Safety page (simulated).")
st.json(profile.__dict__)
