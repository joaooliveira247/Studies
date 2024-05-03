from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.execute("UPDATE clientes SET name=? WHERE id=?;", ("SOMEBODY", 1))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
