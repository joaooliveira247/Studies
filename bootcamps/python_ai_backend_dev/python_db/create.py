from common import get_conn, get_cursor
from sqlite3 import Cursor


def create_table(cursor: Cursor):
    try:
        cursor.execute(
            """
CREATE TABLE IF NOT EXISTS
    clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100),
        email VARCHAR(150)
        );
"""
        )
    except Exception as e:
        print(e)


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    create_table(cur)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
