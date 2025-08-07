# pages/01_Session_Control.py
# Session orchestration: target temp, duration, microbubbles, mixer
# Covers: programmable mixing valve & microbubble jets [oai_citation:11‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import devices, safety

st.title("Session Control")
sys = st.session_state.system

colA, colB = st.columns(2)
with colA:
    target_c = st.slider("Target Cold Temp (°C)", 2.0, 15.0, 8.0)
    minutes  = st.slider("Duration (min)", 1, 20, 5)
    bubbles  = st.toggle("Enable Microbubble Jets", value=True)  # heat transfer accel [oai_citation:12‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
    mix_pct  = st.slider("Hot/Cold Mix (%)", 0, 50, 0)  # programmable mixing valve [oai_citation:13‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
with colB:
    st.write("**Live Status**")
    st.json(sys.dict())

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Start Cold"):
        devices.start_session(sys, target_c=target_c, minutes=minutes, microbubbles=bubbles, mix_pct=mix_pct)
with c2:
    if st.button("Switch to Hot"):
        devices.switch_mode(sys, "HOT")
with c3:
    if st.button("End Session"):
        devices.end_session(sys)

st.progress(int(sys.fill_pct))
st.line_chart(devices.history_df())
