from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.execute("DELETE FROM clientes WHERE id=?;", (2,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
