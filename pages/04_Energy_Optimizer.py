# pages/04_Energy_Optimizer.py
# Predictive chill scheduling from occupancy + history [oai_citation:18‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import optimizer

st.title("Predictive Chill & Energy Optimizer")

occ = st.slider("Hotel Occupancy (%)", 0, 100, 72)
historical = st.slider("Avg Daily Sessions", 0, 50, 18)
stagger = st.toggle("Stagger Multi-Unit Cycles", value=True)  # reduce power spikes [oai_citation:19‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

schedule = optimizer.make_schedule(occ, historical, stagger)
st.subheader("Recommended Pre‑Chill Windows")
st.table(schedule)

kpi = optimizer.estimate_kpis(schedule, occ, historical)
st.subheader("Energy & ESG KPIs")
st.json(kpi)
