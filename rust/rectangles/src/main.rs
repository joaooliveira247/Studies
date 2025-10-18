#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect_1 = Rectangle{width: 30, height: 50};

    println!("rect_1 is {:#?}", rect_1);

    println!("The area of the rectangle is {} square pixels.", area(&rect_1));
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}