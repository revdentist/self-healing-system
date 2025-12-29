def classify_log(message: str) -> str:
    text = message.lower()

    if any(word in text for word in ["database", "sql", "db", "crash", "dropped"]):
        return "database_error"

    if any(word in text for word in ["auth", "login", "unauthorized", "token"]):
        return "authentication_error"

    if any(word in text for word in ["timeout", "slow", "latency"]):
        return "timeout_error"

    return "unknown_error"
