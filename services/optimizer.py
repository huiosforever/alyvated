# services/optimizer.py
# Predictive pre‑chill windows & KPI estimates [oai_citation:32‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:33‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

from datetime import datetime, timedelta
import pandas as pd
from . import devices

def make_schedule(occupancy_pct:int, avg_sessions:int, stagger:bool):
    base = max(1, int(avg_sessions * occupancy_pct/100 * 0.6))
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    wins = []
    for i in range(base):
        start = now + timedelta(hours=1 + i*(1 if stagger else 0))
        wins.append(dict(window=f"{start:%H:%M}-{(start+timedelta(minutes=30)):%H:%M}", units=1))
    return pd.DataFrame(wins)

def estimate_kpis(schedule_df, occ, avg):
    prechill_events = len(schedule_df)
    energy_saved_kwh = round(prechill_events * 0.2, 2)
    peak_shaved_kw = 0.5 if prechill_events>2 else 0.2
    return dict(prechill_events=prechill_events, energy_saved_kwh=energy_saved_kwh, peak_shaved_kw=peak_shaved_kw)

def apply_prechill(sys: devices.SystemState):
    sys.energy_kwh += 0.05
    sys.water_temp_c = max(4.0, sys.water_temp_c - 2.0)
