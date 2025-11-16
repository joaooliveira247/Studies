/*
fn main() {
    let r;

    {
        let x = 5;
        r = &x;
    } // x lifetime expires here

    println!("r: {}", r);
} // r lifetime expires here

*/


fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let string_1 = String::from("abcd");
    let string_2 = "xyz";

    let result = longest(string_1.as_str(), string_2);

    println!("The longest string is {}", result)
}
