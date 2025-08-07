# pages/06_Loyalty_PMS.py
# PMS auth, loyalty tier constraints, folio posting [oai_citation:21‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import pms, devices

st.title("PMS & Loyalty Control")

prof = pms.current_profile()
st.json(prof.__dict__)

st.subheader("Apply Tier Rules")
if st.button("Enforce Session Limits"):
    devices.enforce_tier_limits(st.session_state.system, prof)
    st.success("Applied.")

st.subheader("Post Charge")
amount = st.number_input("Charge (USD)", 0.0, 200.0, 25.0)
if st.button("Post to Folio"):
    ref = pms.post_charge(prof, amount)
    st.success(f"Posted: {ref}")
