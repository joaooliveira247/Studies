#[derive(Debug)]
struct Point {
    x: i32,
    y: i32
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
    let p = Point{ x: 0, y: 7};
    
    match p {
            Point { x, y: 0 } => println!("On the x axis at {x}"),
            Point { x: 0, y } => println!("On the y axis at {y}"),
            Point { x, y } => {
                println!("On neither axis: ({x}, {y})");
            }
        }
}

fn main() {
    destructing_pattern();
}
