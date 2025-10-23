fn main() {

    // string
    let  a  = String::new();

    //string slice
    let greetings = "Hello, world!";

    println!("{} | {}", a, greetings);

    let mut s = String::from("foo");

    s.push_str(" bar");

    println!("{}", s);

    let s2 = String::from("lo");
    s.push('l');

    println!("{}", s2);

    let s3 = String::from("tic");
    let s4 = String::from("tac");
    let s5 = String::from("toc");

    let s6 = s3 + "-" + &s4 + "-" + &s5;

    println!("{}", s6);

    let book_name = String::from("It");
    let author = String::from("Stephen King");
    let publication_year = 1986;

    let book_description = format!("{} - {}({})", book_name, author, publication_year);

    println!("{}", book_description);



}
