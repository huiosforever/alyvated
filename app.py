# Home.py
# Streamlit launcher: dashboard + quick links
# Covers: System overview & session entrypoint

import streamlit as st
from services import devices, safety, optimizer, pms, esg, config

st.set_page_config(
    page_title="Alyvated Dashboard",
    page_icon="🧊",
    layout="wide"
)

if "system" not in st.session_state:
    st.session_state.system = devices.SystemState()

st.title("Alyvated Ice Bath – Feature Demo 🧊")
st.caption("Covers AI safety, ADA access, contrast control, predictive chill, PMS/loyalty, blockchain logging, ESG, and room sync.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Water Temp (°C)", f"{st.session_state.system.water_temp_c:.1f}")
    st.metric("Mode", st.session_state.system.mode)
with col2:
    st.metric("Fill Level (%)", f"{st.session_state.system.fill_pct:.0f}")
    st.metric("Energy (kWh, est.)", f"{st.session_state.system.energy_kwh:.2f}")
with col3:
    st.metric("Session Active", "Yes" if st.session_state.system.active else "No")
    st.metric("Guest Tier", pms.current_profile().tier)

st.subheader("Quick Actions")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("Start Cold Session"):
        devices.start_session(st.session_state.system, target_c=10.0, minutes=3)
with c2:
    if st.button("Start Hot Contrast"):
        devices.switch_mode(st.session_state.system, "HOT")
with c3:
    if st.button("Emergency Drain"):
        devices.emergency_drain(st.session_state.system)
with c4:
    if st.button("Optimize Chill Now"):
        optimizer.apply_prechill(st.session_state.system)

st.info("Use the left sidebar pages to explore individual modules.")
