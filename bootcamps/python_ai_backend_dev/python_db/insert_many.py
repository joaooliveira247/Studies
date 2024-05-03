from common import get_conn, get_cursor


def main() -> None:
    conn = get_conn()
    cur = get_cursor(conn)
    cur.executemany(
        "INSERT INTO clientes (name, email) VALUES (?, ?)",
        [
            ("Sheldon", "sheldon@email.com"),
            ("Leonard", "leonard@email.com"),
            ("Penny", "penny@email.com"),
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
