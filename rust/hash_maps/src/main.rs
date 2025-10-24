use std::collections::HashMap;

fn main() {
    let teams = vec![String::from("Blue"), String::from("Yellow")];

    let initial_scores = vec![10, 50];

    let scores: HashMap<&String, &i32> = teams.iter().zip(initial_scores.iter()).collect();

    println!("{:?}", scores);

    let mut map = HashMap::new();

    map.insert(String::from("Favorite Color"), String::from("Blue"));

    let favorite_color = map.get(&String::from("Favorite Color"));

    if let Some(i) = favorite_color {
        println!("{}", i);
    }

    for (k, v) in &scores {
        println!("{}: {}", k, v);
    }

    let mut scores_2 = HashMap::new();
    scores_2.insert(String::from("Blue"), 10);
    scores_2.insert(String::from("Blue"), 175);

    println!("{:?}", scores);

    scores_2.entry(String::from("Yellow")).or_insert(50);
    scores_2.entry(String::from("Blue")).or_insert(22);

    println!("{:?}", scores_2);

    let text = "hello world wonderful world";

    let mut words = HashMap::new();

    for w in text.split_whitespace() {
        let count = words.entry(w).or_insert(0);
        *count +=1;
    }

    println!("{:?}", words);

}
