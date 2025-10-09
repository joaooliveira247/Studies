fn main() {
    {
        let s = "Hello";
        println!("{}", s);
    }
    /* it don't run 'cause s is out o scope.
    println!("{}", s);
    */

    // the string type

    let mut s = String::from("Hello");
    s.push_str(" world !");

    println!("{}", s);
}
