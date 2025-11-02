struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {

    fn x(&self) -> &T {
        &self.x
    }
    
}


fn largest<T>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list[1..].iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let numbers_list = vec![34, 50, 25, 100, 65];

    let result = largest(&numbers_list);

    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'g'];

    let result = largest(&char_list);

    println!("The largest number is {}", result);

    let integer = Point{x: 5, y: 10};
    let float = Point{x: 1, y: 4.0};
}
