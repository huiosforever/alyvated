# pages/08_Room_Sync.py
# Post-session IoT sync: lights, temp, music [oai_citation:24‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import room_sync, devices

st.title("Room Sync & Recovery Mode")

lights  = st.toggle("Dim Lights", value=True)
temp    = st.slider("Target Room Temp (°C)", 18.0, 26.0, 22.0)
music   = st.selectbox("Ambient", ["Off", "Chill", "Focus", "Sleep"], index=1)

if st.button("Apply Sync Now"):
    result = room_sync.apply({"lights": lights, "temp": temp, "music": music}, devices.last_session())
    st.success(result["message"])
