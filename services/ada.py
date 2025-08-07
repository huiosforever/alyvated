# services/ada.py
# ADA profile storage + gesture toggle [oai_citation:40‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

from dataclasses import dataclass
from . import storage, config

@dataclass
class ADAProfile:
    seat_depth_cm: int = 55
    ramp_angle_deg: int = 8
    fail_safe: bool = True
    gestures: bool = True
    auto_level: bool = True

def get_profile() -> ADAProfile:
    data = storage.load_json(config.ADA_PROFILE_PATH, ADAProfile().__dict__)
    return ADAProfile(**data)

def save_profile(depth:int, angle:int, fail:bool, gestures:bool, auto_level:bool):
    storage.save_json(config.ADA_PROFILE_PATH,
                      dict(seat_depth_cm=depth, ramp_angle_deg=angle, fail_safe=fail, gestures=gestures, auto_level=auto_level))
