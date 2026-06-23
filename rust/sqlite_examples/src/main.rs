use rusqlite::{Connection, Result};

#[derive(Debug)]
struct Customer {
    id: i32,
    name: String,
    phone: String,
}

fn main() -> Result<()> {
    let conn = Connection::open_in_memory()?;

    conn.execute(
        "CREATE TABLE customer (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL)",
        (),
    )?;

    let me = Customer {
        id: 1,
        name: "Steven".to_string(),
        phone: "+1 063 347 8893".to_string(),
    };

    conn.execute(
        "INSERT INTO customer (id, name, phone) VALUES (?1, ?2, ?3)",
        (&me.id, &me.name, &me.phone),
    )?;
    
    let mut stmt = conn.prepare("SELECT id, name, phone FROM customer")?;

    let person_iter = stmt.query_map([], |row| {
        Ok(Customer {
            id: row.get(0)?,
            name: row.get(1)?,
            phone: row.get(2)?,
        })
    })?;

    for person in person_iter {
        println!("Found person {:?}", person.unwrap());
    }

    Ok(())
}
