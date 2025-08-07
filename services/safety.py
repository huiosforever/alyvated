# services/safety.py
# Vitals + gait → emergency / restrict depth [oai_citation:30‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi) [oai_citation:31‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

from dataclasses import dataclass
from . import storage, config

@dataclass
class Thresholds:
    hr_min: int = 40
    spo2_min: int = 85
    motion_timeout_s: int = 10

def load_thresholds() -> Thresholds:
    data = storage.load_json(config.THRESHOLDS_PATH, Thresholds().__dict__)
    return Thresholds(**data)

def save_thresholds(t: Thresholds):
    storage.save_json(config.THRESHOLDS_PATH, t.__dict__)

@dataclass
class Alerts:
    trigger_emergency: bool
    restrict_depth: bool
    notes: str

def evaluate_inputs(hr:int, spo2:int, motion_ok:bool, gait_risk:str) -> Alerts:
    t = load_thresholds()
    emerg = (hr < t.hr_min) or (spo2 < t.spo2_min) or (not motion_ok)
    restrict = gait_risk in ("High",)
    note = []
    if emerg: note.append("Vitals out of envelope.")
    if restrict: note.append("Gait risk high; restrict depth.")
    return Alerts(trigger_emergency=emerg, restrict_depth=restrict, notes=" ".join(note))
