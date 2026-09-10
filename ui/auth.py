import re
import sqlite3
import bcrypt
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent / "users.db"

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = _get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email.strip()))


def email_exists(email: str) -> bool:
    conn = _get_connection()
    row = conn.execute(
        "SELECT 1 FROM users WHERE email = ?", (email.lower().strip(),)
    ).fetchone()
    conn.close()
    return row is not None


def create_user(email: str, password: str):
    email = email.lower().strip()

    if not is_valid_email(email):
        return False, "Please enter a valid email address."

    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    if email_exists(email):
        return False, "An account with this email already exists."

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = _get_connection()
    conn.execute(
        "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
        (email, password_hash.decode("utf-8"), datetime.now(timezone.utc).isoformat()),
    )
    conn.commit()
    conn.close()

    return True, "Account created successfully."


def verify_user(email: str, password: str):
    email = email.lower().strip()

    conn = _get_connection()
    row = conn.execute(
        "SELECT password_hash FROM users WHERE email = ?", (email,)
    ).fetchone()
    conn.close()

    if row is None:
        return False, "No account found with this email."

    stored_hash = row["password_hash"].encode("utf-8")

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        return True, "Login successful."

    return False, "Incorrect password."