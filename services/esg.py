# services/esg.py
# ESG metrics & predictive maintenance [oai_citation:37‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:38‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

import pandas as pd

def compute_esg(df: pd.DataFrame):
    sessions = df[df["event"].str.contains("start_cold", na=False)]
    est_water_l = len(sessions) * 180  # demo: 180 L per session
    est_energy_kwh = df["energy_kwh"].max() if not df.empty else 0
    water_reuse_pct = 35  # demo: gravity/coil recovery [oai_citation:39‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
    return {"sessions": int(len(sessions)), "water_l": est_water_l, "energy_kwh": float(est_energy_kwh), "water_reuse_pct": water_reuse_pct}

def predictive_alerts(df: pd.DataFrame):
    # simple heuristics: hot/cold switch frequency → chiller stress
    switches = df[df["event"].str.contains("switch_", na=False)]
    alerts = []
    if len(switches) > 5:
        alerts.append({"component": "Chiller", "severity": "Medium", "issue": "Frequent cycling detected"})
    if (df["water_temp_c"].max() - df["water_temp_c"].min() if not df.empty else 0) > 25:
        alerts.append({"component": "Mixer Valve", "severity": "Low", "issue": "Wide temp swings"})
    if not alerts:
        alerts.append({"component": "System", "severity": "OK", "issue": "No anomalies"})
    return pd.DataFrame(alerts)
