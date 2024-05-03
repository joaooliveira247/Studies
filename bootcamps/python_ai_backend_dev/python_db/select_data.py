from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.execute("SELECT * FROM clientes;")
    print(cur.fetchone())

    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main()
