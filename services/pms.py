# services/pms.py
# PMS profile, tier rules, folio posting [oai_citation:36‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

from dataclasses import dataclass
import uuid

@dataclass
class Profile:
    guest_id: str
    name: str
    tier: str  # Standard, Silver, Gold, Platinum
    room: str

def current_profile() -> Profile:
    return Profile(guest_id="GUEST-001", name="Demo Guest", tier="Silver", room="1207")

def post_charge(profile: Profile, amount: float) -> str:
    # demo: returns a reference id
    return f"FOLIO-{profile.room}-{str(uuid.uuid4())[:6]}-${amount:.2f}"
