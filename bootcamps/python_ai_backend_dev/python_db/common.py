import sqlite3
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(f"{BASE_DIR / 'teste.db'}")
    return conn


def get_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    return conn.cursor()
