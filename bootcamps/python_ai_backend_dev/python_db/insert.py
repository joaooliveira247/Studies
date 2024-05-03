from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.execute(
        "INSERT INTO clientes (name, email) VALUES (?, ?);",
        ("noobdy", "nobody@email.com"),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
