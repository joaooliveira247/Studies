fn main() {
    println!("Hello, world!");
    // if_statment();
    // loop_statment();
    for_loop();
}

#[allow(dead_code)]
fn if_statment() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 4");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }

    let condition = true;
    let number_2 = if condition {
        5
    } else {6};

    println!(" number_2 is {}", number_2);
}

#[allow(dead_code)]
fn loop_statment() {
    loop {
        println!("Hello");
    }
}

#[allow(dead_code)]
fn while_loop() {
    /*
    let mut counter = 3;
    while counter > 0 {
        println!("Counter: {}", counter);
        counter -= 1;
    }
    println!("LIFTOFF!!!");
    */
    let a = [10, 5, 18, 26, 32];
    let mut counter = 0;

    while counter < a.len() {
        println!("{}", a[counter]);
        counter += 1;
    }
}

fn for_loop() {
    let a = [10, 5, 18, 26, 32];

    for item in a.iter() {
        println!("{}", item);
    }

    for n in (1..4).rev() {
        println!("{}", n);
    }
}