# services/devices.py
# Simulated hardware: tub, chiller, drain, mixer, microbubbles [oai_citation:25‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:26‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:27‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

from dataclasses import dataclass, asdict
import pandas as pd
import time, uuid, os
from . import config

@dataclass
class SystemState:
    mode: str = "COLD"
    water_temp_c: float = 18.0
    fill_pct: float = 25.0
    active: bool = False
    energy_kwh: float = 0.00

    def dict(self): return asdict(self)

_history_cols = ["ts","mode","water_temp_c","fill_pct","energy_kwh","event","session_id"]
def _history_path(): return config.HISTORY_PATH

def _append(event, sys, session_id=None):
    row = dict(ts=time.time(), mode=sys.mode, water_temp_c=sys.water_temp_c,
               fill_pct=sys.fill_pct, energy_kwh=sys.energy_kwh, event=event, session_id=session_id)
    df = history_df()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(_history_path(), index=False)

def history_df():
    if not os.path.exists(_history_path()):
        pd.DataFrame(columns=_history_cols).to_csv(_history_path(), index=False)
    return pd.read_csv(_history_path())

_last_session = {"session_id": None, "target_c": None, "minutes": None}

def start_session(sys: SystemState, target_c: float, minutes: int, microbubbles=True, mix_pct=0):
    sys.active = True
    sys.mode   = "COLD"
    sys.fill_pct = min(100.0, sys.fill_pct + 30.0)
    # naive temp pull-down proportional to mix
    sys.water_temp_c = max(target_c, sys.water_temp_c - (6 - mix_pct/10))
    sys.energy_kwh += 0.15
    sid = str(uuid.uuid4())[:8]
    _append(f"start_cold(bubbles={microbubbles},mix={mix_pct})", sys, sid)
    _last_session.update(session_id=sid, target_c=target_c, minutes=minutes)

def switch_mode(sys: SystemState, mode: str):
    sys.mode = mode
    if mode == "HOT":
        sys.water_temp_c = min(40.0, sys.water_temp_c + 8)
    _append(f"switch_{mode.lower()}", sys, _last_session["session_id"])

def end_session(sys: SystemState):
    sys.active = False
    sys.fill_pct = max(10.0, sys.fill_pct - 20.0)
    _append("end", sys, _last_session["session_id"])

def emergency_drain(sys: SystemState):
    sys.active = False
    sys.fill_pct = 0.0
    sys.water_temp_c = min(25.0, sys.water_temp_c + 5.0)  # thermal mitigation [oai_citation:28‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
    _append("emergency_drain", sys, _last_session["session_id"])

def reduce_depth(sys: SystemState):
    sys.fill_pct = min(sys.fill_pct, 40.0)
    _append("restrict_depth", sys, _last_session["session_id"])

def enforce_tier_limits(sys: SystemState, profile):
    if profile.tier in ("Standard","Silver"):
        # restrict very low temps for safety & tier policy [oai_citation:29‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)
        sys.water_temp_c = max(sys.water_temp_c, 8.0)
    _append("tier_enforced", sys, _last_session["session_id"])

def apply_mixer(sys: SystemState, mix_pct: int):
    sys.water_temp_c += mix_pct * 0.05
    _append(f"mixer_{mix_pct}", sys, _last_session["session_id"])

def last_session():
    return dict(_last_session)
