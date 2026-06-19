use uuid::Uuid;

use crate::services;
use std::{
    io::{self, Read},
    process::Command,
    thread,
    time::Duration,
};

pub fn create_customer() {
    clean_screen();
    let (mut name, mut phone) = (String::new(), String::new());

    println!("Customer name:");
    io::stdin()
        .read_to_string(&mut name)
        .expect("Error when try read name.");

    println!("Customer phone number");
    io::stdin()
        .read_to_string(&mut phone)
        .expect("Error when try read phone number.");

    services::customers::create(&name.trim(), &phone.trim())
        .expect("Error when try create customer");
    println!("Customer created!");
    wait_seconds(2);
    clean_screen();
}

pub fn show_customers() -> Result<(), std::io::Error> {
    clean_screen();
    let customers = services::customers::show_customers()?;
    for customer in &customers {
        println!("----------------------");
        println!("ID: {}", customer.id);
        println!("ID: {}", customer.name);
        println!("ID: {}", customer.phone);
        println!("----------------------");
    }
    println!("----------------------");
    wait_enter();
    clean_screen();

    Ok(())
}

fn wait_enter() {
    println!("Press Enter to continue");
    let mut _trash = String::new();
    io::stdin()
        .read_to_string(&mut _trash)
        .expect("Error when try read input.");
    clean_screen();
}

fn clean_screen() {
    if cfg!(target_os = "windows") {
        Command::new("cmd")
            .args(["/C", "cls"])
            .status()
            .expect("Failed to clean terminal.");
    } else {
        Command::new("clear")
            .status()
            .expect("Failed to clean terminal.");
    }
}

fn wait_seconds(t: u64) {
    thread::sleep(Duration::from_secs(t));
}

pub fn update_customer() -> Result<(), std::io::Error> {
    clean_screen();
    let (mut id, mut name, mut phone) = (String::new(), String::new(), String::new());

    println!("Customer ID to update.");
    io::stdin()
        .read_to_string(&mut id)
        .expect("Error when try read ID.");
    let id: Uuid = id
        .trim()
        .parse()
        .expect(format!("ID: {} is not a valid ID.", id).as_str());

    println!("Customer name to update.");
    io::stdin()
        .read_to_string(&mut name)
        .expect("Error when try read name.");

    println!("Customer phone to update.");
    io::stdin()
        .read_to_string(&mut phone)
        .expect("Error when try read name.");

    services::customers::update(id, &name.trim(), &phone.trim())?;
        .expect("Error when try update customer.");
    wait_seconds(2);
    clean_screen();

    Ok(())
}

pub fn delete_customer() -> Result<(), io::Error> {
    clean_screen();
    let mut id = String::new();

    io::stdin()
        .read_to_string(&mut id)
        .expect("Error when try read ID.");
    let id: Uuid = id
        .trim()
        .parse()
        .expect(format!("ID: {} is not a valid ID.", id).as_str());

    services::delete(id).expect("Error when try delete customer.");
    println!("Customer excluded.");
    wait_seconds(2);
    clean_screen();

    Ok(())
}
