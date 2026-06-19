use std::io::{self, Read};

fn main() {
    loop {
        println!(
            "\
            CRUD Customers
            1. Create customer
            2. Show customers
            3. Update customer
            4. Del customer
            5. Exit
            "
        );

        let mut choice = String::new();

        io::stdin()
            .read_to_string(&mut choice)
            .expect("Error when try read input.");

        let num_choice: u8 = choice
            .trim()
            .parse()
            .expect(format!("Expected a number, get: {}", choice).as_str());

        match num_choice {
            1 => display::create_customer(),
            2 => {
                if let Err(e) = display::show_customers() {
                    println!(format!("Error when try show customers: {}", e))
                }
            }
            3 => {
                if let Err(e) = display::update_customer {
                    println!(format!("Error when try update customers {}", e))
                }
            },
            4 => {
                if let Err(e) = display::delete_customer() {
                    println!(format!("Error when try delete customers: {}", e))
                }
            }
            5 => break,
        }
    }
}
