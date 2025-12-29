def send_alert(entry: dict):
    print("\n INCIDENT ALERT!")
    print(f"ID: {entry.get('id')}")
    print(f"TYPE: {entry.get('type')}")
    print(F"MESSAGE: {entry.get('message')}")
    print(F"CATEGORY: {entry.get('category')}")
    print("--------------------------------------------------\n")