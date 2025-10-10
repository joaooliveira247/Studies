fn main() {
    let s1 = String::from("Hello Reference");

    println!("{}: {} len", s1, calculate_length(&s1))
}

fn calculate_length(s: &String) -> usize {
    s.len()
}