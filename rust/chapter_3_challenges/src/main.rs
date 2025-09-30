use std::io;

fn main() {
    // temperature_converter();
    // let fib_sum = fib(21);
    // println!("{}", fib_sum);
}

#[allow(dead_code)]
fn temperature_converter() {
    println!("Select temperature to convert (F)Fahrenheit or (C)Celsius");
    println!("Select (F)Fahrenheit will convert temperature to Celsius");
    println!("Select (C)Celcius will convert temperature to Fahrenheit");

    let mut option = String::new();

    io::stdin()
        .read_line(&mut option)
        .expect("Failed to read option");

    let option = option.trim().to_lowercase();

    let mut temperature = String::new();

    println!("Type º{} temperature", option);

    io::stdin()
        .read_line(&mut temperature)
        .expect("Failed to read temperature");

    let temperature: f64 = match temperature.trim().parse() {
        Ok(temp) => temp,
        Err(_) => panic!("{} is not a valid value to temperature", temperature),
    };

    match option.as_str() {
        "c" => {
            let fahrenheit = ((9.0 * temperature) + (5.0 * 32.0)) / 5.0;
            println!("{} ºF", fahrenheit);
        }
        "f" => {
            let celcius = ((5.0 * temperature) - (5.0 * 32.0)) / 9.0;
            println!("{} ºF", celcius);
        }
        _ => println!("Invalid option"),
    }
}

fn fib(n: u8) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2)
    }
}