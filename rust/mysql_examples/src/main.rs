use mysql::{params, prelude::Queryable};
use mysql_examples::{config, models::customers::Customer};
use std::result::Result;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut conn = config::conn::get_connection()?;
    println!("Hello, world!");

    /* Create
    conn.query_drop(
        r"CREATE TABLE IF NOT EXISTS customers (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(255),
            phone VARCHAR(255),
            PRIMARY KEY (id)
        );",
    )?;
    */

    /* Insert
    conn.exec_drop(
        r"INSERT INTO customers (name, phone) VALUES (:name, :phone)",
        params! {"name" => "Robert Hills", "phone" => "+55 21 12345-6789"},
    )?;
    */

    /* read all
    let customers: Vec<Customer> = conn.query_map(
        r"SELECT id, name, phone FROM customers;",
        |(id, name, phone)| Customer { id, name, phone },
    )?;
    */

    // UPDATE
    // conn.exec_drop(
    //     "UPDATE customers SET name = :name, phone = :phone WHERE id = :id;",
    //     params! {"name" => "Carlos", "phone" => "+55 21 91234-5678", "id" => 3},
    // )?;
    //

    // Select One
    // let customer: Option<Customer> = conn
    //     .exec_first(
    //         "SELECT * FROM customers WHERE id = :id;",
    //         params! {"id" => 3},
    //     )?
    //     .map(|(id, name, phone)| Customer { id, name, phone });

    // println!("{:?}", customer);
    //
    // Delete
    conn.exec_drop("DELETE FROM customers WHERE id = :id;", params! {"id" => 2})?;

    Ok(())
}
