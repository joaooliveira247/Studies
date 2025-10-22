#[derive(Debug)]
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

fn main() {
    // empty vector
    // let v: Vec<i32> = Vec::new();

    // macro vector to create vector with valies
    // let v = vec![1, 2, 3, 4];

    /*
    let mut v = Vec::new();
    v.push(5);
    v.push(2);
    v.push(6);
    v.push(7);
    println!("{:?}", v);
    v[2] = 96;
    println!("{:?}", v);
    */

    /*
    {
        let v = vec![1, 2, 3, 4];

        
    } // v is out of scope here
    */

    // let v = vec![1, 2, 3, 4, 5];

    // let second = &v[2];
    // let third = v.get(2);

    /*
    // iter by a vec

    let v = vec![1, 2, 3, 4, 5];

    for i in &v {
        println!("{}", i);
    }
    */

    /*
    // iter by a mut vec

    let mut v = vec![1, 2, 3, 4];

    for i in &mut v {
        *i += 50;
    }

    println!("{:?}", v);
    */

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

    println!("{:?}", row);

    
}
