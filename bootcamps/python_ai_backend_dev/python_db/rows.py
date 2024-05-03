from common import get_conn, get_cursor
from sqlite3 import Row


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.row_factory = Row
    cur.execute("SELECT * FROM clientes;")

    for row in cur.fetchall():
        print(dict(row))

    conn.close()


if __name__ == "__main__":
    main()
