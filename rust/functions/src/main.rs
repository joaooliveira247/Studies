fn main() {
    println!("Hello, world!");
    another_function(5, 6);

    let x= 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("x is {}, y is {}", x, y);

    let z = five();

    println!("z is {}", z);

}

fn another_function(x: u8, y: u8) {
    println!("x: {}, y: {}", x, y);
}

fn five() -> u8 {
    5
}