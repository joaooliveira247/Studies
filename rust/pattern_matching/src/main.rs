#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

#[derive(Debug)]
enum MessageBinding {
    Hello { id: i32 },
}

#[derive(Debug)]
enum Color {
    Rgb(i32, i32, i32),
    Hsv(i32, i32, i32),
}

#[derive(Debug)]
enum NestedMessage {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(Color),
}

#[derive(Debug)]
#[allow(dead_code)]
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

#[allow(dead_code)]
fn literals() {
    let x = 1;

    match x {
        1 => println!("one"),
        2 => println!("one"),
        3 => println!("one"),
        _ => println!("one"),
    };
}

#[allow(dead_code)]
fn named_variables() {
    let x = Some(5);

    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(y) => println!("Matched y = {y}",),
        _ => println!("Default case x = {x:?}",),
    }

    println!("at the end x = {x:?}, y = {y}");
}

#[allow(dead_code)]
fn multiple_patterns() {
    let x = 1;

    match x {
        1 | 2 => println!("one or two"),
        3 => println!("three"),
        _ => println!("anything"),
    }
}

#[allow(dead_code)]
fn range_pattern() {
    let x = 56;

    match x {
        ..51 => println!("lt 50"),
        51..100 => println!("gt 51, lt 100"),
        _ => println!("something else"),
    }
}

#[allow(dead_code)]
fn destructing_pattern() {
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("On the x axis at {x}"),
        Point { x: 0, y } => println!("On the y axis at {y}"),
        Point { x, y } => {
            println!("On neither axis: ({x}, {y})");
        }
    }
}

#[allow(dead_code)]
fn enum_pattern() {
    let msg = Message::ChangeColor(0, 160, 255);

    match msg {
        Message::Quit => {
            println!("The Quit variant has no data to destructure.");
        }
        Message::Move { x, y } => {
            println!("Move in the x direction {x} and in the y direction {y}");
        }
        Message::Write(text) => {
            println!("Text message: {text}");
        }
        Message::ChangeColor(r, g, b) => {
            println!("Change color to red {r}, green {g}, and blue {b}");
        }
    }
}

#[allow(dead_code)]
fn nested_struct_enums() {
    let msg = NestedMessage::ChangeColor(Color::Hsv(0, 160, 255));

    match msg {
        NestedMessage::ChangeColor(Color::Rgb(r, g, b)) => {
            println!("Change color to red {r}, green {g}, and blue {b}");
        }
        NestedMessage::ChangeColor(Color::Hsv(h, s, v)) => {
            println!("Change color to hue {h}, saturation {s}, value {v}");
        }
        _ => (),
    }
}

#[allow(dead_code)]
fn parts_of_values() {
    let mut setting_value = Some(5);
    let new_setting_value = Some(10);

    match (setting_value, new_setting_value) {
        (Some(_), Some(_)) => {
            println!("Can't overwrite an existing customized value");
        }
        _ => {
            setting_value = new_setting_value;
        }
    }

    println!("setting is {setting_value:?}");
}

#[allow(dead_code)]
fn remaining_parts() {
    let origin = Point { x: 0, y: 0 };

    match origin {
        Point { x, .. } => println!("x is {x}"),
    }

    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first, .., last) => {
            println!("Some numbers: {first}, {last}");
        }
    }
}

#[allow(dead_code)]
fn match_guards() {
    let num = Some(4);

    match num {
        Some(x) if x % 2 == 0 => println!("The number {x} is even"),
        Some(x) => println!("The number {x} is odd"),
        None => (),
    }
}

#[allow(dead_code)]
fn binding() {
    let msg = MessageBinding::Hello { id: 5 };

    match msg {
        MessageBinding::Hello { id: id @ 3..=7 } => {
            println!("Found an id in range: {id}")
        }
        MessageBinding::Hello { id: 10..=12 } => {
            println!("Found an id in another range")
        }
        MessageBinding::Hello { id } => println!("Found some other id: {id}"),
    }
}

fn main() {
    enum_pattern();
}
