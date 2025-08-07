# services/blockchain.py
# Local JSON "ledger" + fake NFT mint [oai_citation:34‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:35‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import uuid, time, pandas as pd, os
from . import storage, config

def _ledger():
    return storage.load_json(config.LEDGER_PATH, {"tx": []})

def _save(led):
    storage.save_json(config.LEDGER_PATH, led)

def log_session(sess):
    led = _ledger()
    tx = {"tx_id": str(uuid.uuid4())[:8], "ts": time.time(), "session": sess}
    led["tx"].append(tx)
    _save(led)
    return tx

def mint_nft(sess):
    token_id = "NFT-" + str(uuid.uuid4())[:8]
    rec = {"token_id": token_id, "wallet": config.DEFAULT_WALLET, "session": sess, "ts": time.time()}
    led = _ledger(); led["tx"].append({"mint": rec}); _save(led)
    return rec

def ledger_df():
    led = _ledger()
    flat = []
    for item in led["tx"]:
        t = {"type": "tx" if "tx_id" in item else "mint", **item}
        flat.append(t)
    return pd.DataFrame(flat)
