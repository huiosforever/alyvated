# pages/07_Maintenance_ESG.py
# Predictive maintenance + ESG dashboard [oai_citation:22‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:23‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import esg, devices

st.title("Maintenance & ESG")

alerts = esg.predictive_alerts(devices.history_df())
st.subheader("Maintenance Alerts")
st.table(alerts)

st.subheader("ESG Dashboard (Water & Energy)")
metrics = esg.compute_esg(devices.history_df())
st.json(metrics)
