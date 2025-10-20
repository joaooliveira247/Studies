/*
#[derive(Debug)]
enum IpAddrKind {
    V4,
    V6,
}

#[derive(Debug)]
struct IpAddr {
    kind: IpAddrKind,
    address: String
}

fn main() {
    let home = IpAddr{
        kind: IpAddrKind::V4,
        address : String::from("127.0.0.1")
    };

    let loopback = IpAddr{
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };

    println!("{:#?} | {:#?}", home, loopback)
}
*/
#[derive(Debug)]
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

enum Message {
    Quit,
    Move{ x: i32, y: i32},
    Write(String),
    ChangeColor(i32, i32, i32),
}

struct QuitMessage; // Unit struct

struct MoveMessage {
    x: i32,
    y: i32,
}

struct WriteMessage(String); // tuple struct

struct ChangeColorMessage(i32, i32, i32); // tuple struct

impl Message {
    fn call(&self) {
        
    }
}

fn main() {
    let home = IpAddr::V4(127, 0, 0, 1);

    let loopback = IpAddr::V6(String::from("::1"));

    println!("{:#?} | {:#?}", home, loopback);

    let m = Message::Write(String::from("Hello"));
    m.call();
}