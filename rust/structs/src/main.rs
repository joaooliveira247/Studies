struct User{
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

struct Color(i32, i32, i32);

struct Point(i32, i32, i32);

#[allow(dead_code)]
fn build_user(email: String, username: String) -> User {
    User { username, email, sign_in_count: 1, active: true }
}

#[allow(dead_code)]
fn structs() {
    let mut user_1 = User{
        email: String::from("Someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    println!("{}", user_1.email);

    user_1.email = String::from("AnotherOneEmail@example.com");

    println!("{}", user_1.email);

    // struct update syntax

    let user_2 = User{
        email: String::from("another@example.com"),
        username: String::from("anotherusername567"),
        ..user_1
    };

    // tuple struct

    let black = Color(0, 0, 0);

    let origin = Point(0, 0, 0);

}


fn main() {
    
}
