from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "INSERT INTO clientes (id, name, email) VALUES (id=?,name=?,email=?)",
            (2, "SomeOne", "someone@email.com"),
        )
        conn.commit()
    except Exception as err:
        print(f"[ERROR]: {err}")
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
