# pages/05_Blockchain_Ledger.py
# Immutable logging + NFT reward mint (simulated) [oai_citation:20‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import streamlit as st
from services import blockchain, devices

st.title("Blockchain Ledger & Wellness NFT")

if st.button("Record Current Session"):
    tx = blockchain.log_session(devices.last_session())
    st.success(f"Logged TX: {tx['tx_id']}")

if st.button("Mint Wellness NFT"):
    nft = blockchain.mint_nft(devices.last_session())
    st.success(f"Minted NFT: {nft['token_id']} → {nft['wallet']}")

st.subheader("Ledger")
st.dataframe(blockchain.ledger_df(), use_container_width=True)
