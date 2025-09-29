fn main() {
    // integers
    let num_1 = -8;
    let num_2: u32 = 16_000;
    println!("integer {}, unsigned(without -) {}", num_1, num_2);
    // floats
    let num_3 = 8.0;
    let num_4: f32 = 2.0;
    println!("f64(default): {}, f32(annotated): {}", num_3, num_4);
    // operations
    let sum = 5 + 10;
    let sub = 32 - 16;
    let mult = 3 * 2;
    let div = 64 / 16;
    let remainder = 9 % 2;
    println!(
        "sum: {}, sub: {}, mult: {}, div: {}, remainder: {}",
        sum, sub, mult, div, remainder
    );
    // boleans
    let t = true;
    let f: bool = false;
    // char type
    println!("true: {}, false: {}", t, f);
    let emoji = '😻';
    println!("{}", emoji);
    // tuple
    let tup: (u8, char, &'static str) = (8, '😻', "Hello");
    let (_,y,_) = tup;
    println!("{}, {}", y, tup.0);
    // array
    let a = [1, 2, 3, 4];
    println!("{:?}", a);
    let first = a[0];
    let last= a[a.len() - 1];
    println!("first: {}, last: {}", first, last);
}
