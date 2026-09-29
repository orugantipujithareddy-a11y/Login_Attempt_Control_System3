# Login Attempt Control System

## Overview
A Python-based authentication control mechanism that tracks failed login attempts and temporarily locks an account after repeated failures. The project demonstrates basic protection against simulated brute-force login attempts.

## Objective
- Track failed login attempts by username.
- Enforce a temporary 15-minute account lockout after 5 consecutive failures.
- Record successful, failed, and blocked login events.
- Test the lockout mechanism using simulated repeated login attempts.

## Project Files
- `login_attempt_control.py` — Source code implementing login tracking and lockout logic.
- `test_logs.txt` — Sample execution/test logs showing lockout enforcement.
- `README.md` — Project documentation.

## How the System Works
1. A user attempts to log in.
2. A failed password increments the user's failure counter.
3. After 5 consecutive failures, the account is locked for 15 minutes.
4. Login attempts during the lockout period are rejected.
5. Each event is written to an audit log.
6. A correct password resets the failure counter when the account is not locked.

## Run the Program
```bash
python login_attempt_control.py
```

## Sample Test
The program simulates five incorrect passwords for the `admin` account and then attempts a login while the account is locked.

### Expected Test Log
```text
=== LOGIN ATTEMPT CONTROL SYSTEM ===
LOGIN_FAILED attempt=1
LOGIN_FAILED attempt=2
LOGIN_FAILED attempt=3
LOGIN_FAILED attempt=4
LOGIN_FAILED attempt=5
ACCOUNT_LOCKED for 15 minutes
LOGIN_BLOCKED_LOCKED_ACCOUNT

RESULT: Account lockout enforced successfully after 5 consecutive failed attempts.
```

## Security Features
- Failed-login counter
- 5-attempt lockout threshold
- 15-minute temporary lockout
- Login event auditing
- Unknown-user failure logging
- Protection against repeated password-guessing attempts

## Testing Result
The simulated brute-force loop successfully triggers the configured lockout after the fifth consecutive failed login attempt. A subsequent login is blocked while the account remains locked.

## Note
This is an educational demonstration. For production authentication systems, passwords should never be stored as plaintext; use a secure password-hashing mechanism, persistent storage, rate limiting, and other appropriate authentication controls.

## Submission Proof
The source code and test logs demonstrate account lockout enforcement as required by the project instructions.
