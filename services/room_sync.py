# services/room_sync.py
# Post-session in-room sync (lights, temp, music) [oai_citation:41‡IceBathprovisionalfinaldraft07272025.docx](file-service://file-WqBrfJeywJi439LRUtshTi)

def apply(prefs: dict, session: dict):
    # stub: pretend we called room IoT APIs
    return {"ok": True, "message": f"Applied room sync: {prefs} for session {session.get('session_id','-')}"}
