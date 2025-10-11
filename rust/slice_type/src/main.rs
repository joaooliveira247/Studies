fn main() {
    slicing();
}

fn slicing() {
    let s = String::from("Hello World");
    let hello = &s[..5];
    let world = &s[6..];
    let slice = &s[..];
    println!("{} {} | {}", hello, world, slice);
}

#[allow(dead_code)]
fn first_word_exec() {
    let mut s = String::from("Hello World");
    let word = first_word(&s);

    println!("{}", word);

    s.clear();
}

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return  i;
        }
    }

    s.len()
}