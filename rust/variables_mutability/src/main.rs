const MAX_POINTS: u32 = 100_000;

fn main() {
    // Code don't compile 'cause x is immutable
    /*
    let x = 5;
    println!("x is {}", x);
    x = 6;
    println!("x is {}", x);
    */

    let mut x = 5;

    println!("x is {}", x);

    x = 6;

    println!("x is {}", x);

    // consts

    println!("{}", MAX_POINTS);

    // shadowing

    let y = 5;

    println!("{}", y);

    let y = y + 1;
    println!("{}", y);


    let y = y * 2;
    println!("{}", y);

}
