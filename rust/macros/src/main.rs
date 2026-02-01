macro_rules! say_hi {
    ($name: expr) => {
        println!("hi {}", $name);
    };
}

macro_rules! my_vec {
    ($( $x: expr ), *) => {
        {
        let mut v = Vec::new();
        $(
            v.push($x);
        )*
        v
        }
    };
}

#[allow(unused_macros)]
macro_rules! teste {
    () => {
        println!("Nada passado");
    };
    ($x:expr) => {
        println!("Um valor: {}", $x);
    };
    ($x:expr, $y:expr) => {
        println!("Dois valores: {} e {}", $x, $y);
    };
}

#[allow(unused_macros)]
macro_rules! meu_println {
    ($($arg:tt)*) => {
        println!($($arg)*);
    };
}

fn main() {
    say_hi!("John");
    let v = my_vec!(1, 2, 3, 4, 5);
    println!("{:?}", v);
}
