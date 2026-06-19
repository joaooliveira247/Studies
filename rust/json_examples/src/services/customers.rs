use std::{
    fs::{File, OpenOptions},
    io::{Read, Write},
};

use uuid::Uuid;

use crate::models::customer::Customer;

const CUSTOMERS_JSON: &str = "db/customers.json";

pub fn create(name: &str, phone: &str) -> std::io::Result<()> {
    let mut file =
        File::open(CUSTOMERS_JSON).unwrap_or_else(|_| File::create(CUSTOMERS_JSON).unwrap());
    let mut data = String::new();

    file.read_to_string(&mut data)?;
    drop(file);

    let mut customers: Vec<Customer> = serde_json::from_str(&data).unwrap_or_else(|_| Vec::new());

    let new_customer = Customer {
        id: Uuid::new_v4(),
        name: name.to_string(),
        phone: phone.to_string(),
    };

    customers.push(new_customer);

    let data_json = serde_json::to_string(&customers)?;

    let mut file_write = OpenOptions::new()
        .write(true)
        .truncate(true)
        .open(CUSTOMERS_JSON)?;
    file_write.write_all(&data_json.as_bytes())?;

    Ok(())
}

pub fn show_customers() -> std::io::Result<Vec<Customer>> {
    let mut file = File::open(CUSTOMERS_JSON)?;
    let mut data = String::new();

    file.read_to_string(&mut data)?;
    drop(file);

    let customers: Vec<Customer> = serde_json::from_str(&data)?;

    Ok(customers)
}

pub fn update_customer(id: Uuid, new_name: String, new_phone: String) -> Result<(), std::io::Error> {
    let mut file = File::open(CUSTOMERS_JSON).unwrap_or_else(|_| File::create(CUSTOMERS_JSON)?;
        let mut data = String::new();
        file.read_to_string(&mut contents)?;
        drop(archive_read);

        let mut customers: Vec<Client> = serde_json::from_str(&contents).unwrap_or_else(|_| Vec::new());

        if let Some(customer) = customers.iter_mut().find(|c| c.id == id) {
            if let Some(new_name) = name {
                customer.name = new_name;
            }
            if let Some(new_email) = email {
                customer.phone = new_phone;
            }
        }

        let data_json = serde_json::to_string(&customers)?;
        let mut file_write = OpenOptions::new()
            .write(true)
            .truncate(true)
            .open(CUSTOMERS_JSON)?;

        archive_write.write_all(data_json.as_bytes())?;
        Ok(())
}

pub fn delete(id: Uuid) -> Result<(), std::io::Error> {
    let mut archive_read = File::open(CLIENTS_JSON)?;
        let mut contents = String::new();
        archive_read.read_to_string(&mut contents)?;
        drop(archive_read);

        let mut customers: Vec<Client> = serde_json::from_str(&contents)?;

        clients.retain(|c| c.id != id);

        let data_json = serde_json::to_string(&customers)?;
        let mut archive_write = OpenOptions::new()
            .write(true)
            .truncate(true)
            .open(CLIENTS_JSON)?;

        archive_write.write_all(data_json.as_bytes())?;
        Ok(())
}
