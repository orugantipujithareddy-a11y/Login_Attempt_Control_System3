import time
from datetime import datetime, timedelta

MAX_FAILURES = 5
LOCKOUT_MINUTES = 15

users = {
    "admin": {
        "password": "SecureDemo123!",
        "failed_attempts": 0,
        "locked_until": None
    }
}

audit_log = []

def log_event(username, event):
    entry = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {username} | {event}"
    audit_log.append(entry)
    print(entry)

def login(username, password):
    user = users.get(username)

    if not user:
        log_event(username, "LOGIN_FAILED_UNKNOWN_USER")
        return False

    now = datetime.now()

    if user["locked_until"] and now < user["locked_until"]:
        remaining = int((user["locked_until"] - now).total_seconds())
        log_event(username, f"LOGIN_BLOCKED_LOCKED_ACCOUNT ({remaining}s remaining)")
        return False

    if password == user["password"]:
        user["failed_attempts"] = 0
        user["locked_until"] = None
        log_event(username, "LOGIN_SUCCESS")
        return True

    user["failed_attempts"] += 1
    log_event(username, f"LOGIN_FAILED attempt={user['failed_attempts']}")

    if user["failed_attempts"] >= MAX_FAILURES:
        user["locked_until"] = now + timedelta(minutes=LOCKOUT_MINUTES)
        log_event(username, f"ACCOUNT_LOCKED for {LOCKOUT_MINUTES} minutes")

    return False

if __name__ == "__main__":
    print("=== LOGIN ATTEMPT CONTROL SYSTEM ===")

    # Simulated brute-force attempts
    for i in range(1, 6):
        login("admin", f"wrong-password-{i}")

    # Attempt while account is locked
    login("admin", "SecureDemo123!")

    print("\n=== SECURITY AUDIT LOG ===")
    for entry in audit_log:
        print(entry)
