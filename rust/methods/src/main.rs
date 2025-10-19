#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, another: &Rectangle) -> bool {
        return self.area() >= another.area();
    }
}

impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle { width:size, height: size }
    }
}

fn main() {
    let rect_1 = Rectangle{width: 30, height: 50};
    let rect_2 = Rectangle{width: 10, height: 40};
    let rect_3 = Rectangle{width: 60, height: 45};
    let rect_4 = Rectangle::square(36);

    println!("The area of the rectangle is {} square pixels", rect_1.area());
    println!("The area of the rectangle is {} square pixels", rect_4.area());

    println!("Can rect_1 hold rect_2? {}", rect_1.can_hold(&rect_2));
    println!("Can rect_1 hold rect_3? {}", rect_1.can_hold(&rect_3));
}
