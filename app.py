# app.py
# Streamlit launcher: dashboard + quick links
# Covers: System overview & session entrypoint [oai_citation:6‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import devices, safety, optimizer, pms, esg, config
st.set_page_config(
    page_title="Alyvated Dashboard",
    page_icon="🧊",
    layout="wide"
)

st.set_page_config(page_title="Alyvated Ice Bath Demo", page_icon="🧊", layout="wide")

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
        devices.start_session(st.session_state.system, target_c=10.0, minutes=3)  # demo default [oai_citation:7‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
with c2:
    if st.button("Start Hot Contrast"):
        devices.switch_mode(st.session_state.system, "HOT")  # dual-mode [oai_citation:8‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
with c3:
    if st.button("Emergency Drain"):
        devices.emergency_drain(st.session_state.system)  # safety override [oai_citation:9‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
with c4:
    if st.button("Optimize Chill Now"):
        optimizer.apply_prechill(st.session_state.system)  # predictive chill [oai_citation:10‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

st.info("Use the left sidebar pages to explore individual modules.")
