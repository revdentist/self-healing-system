def is_incident(entry: dict) -> bool:
    message = entry.get("message", "").lower()
    category = entry.get("category", "").lower()

    critical_keywords = [
        "critical", "panic", "fatal", "crash", "kernel panic",
        "catastrophic failure", "system halt", "service down"
    ]
    if any(word in message for word in critical_keywords):
        return True

    database_terms = ["db error", "database crash", "sql fail", "query timeout", "connection refused"]
    if "database" in category or any(term in message for term in database_terms):
        return True

    auth_terms = ["auth failed", "token expired", "unauthorized", "login denied"]
    if "auth" in category or any(term in message for term in auth_terms):
        return True

    if "timeout" in message or "memory leak" in message or "cpu" in message:
        return True

    network_terms = ["dns fail", "network unreachable", "connection dropped", "packet loss"]
    if any(term in message for term in network_terms):
        return True

    return False
