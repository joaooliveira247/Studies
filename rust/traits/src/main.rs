use std::fmt::{self, Debug, Display};

pub trait Summary {
    fn summarize(&self) -> String;

    fn summarize_2(&self, text: String) -> String {
        format!("Summarize_2: {text}")
    }
}

#[derive(Debug)]
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle  {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }    
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet  {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

impl Tweet {
    fn new(username: String, content: String) -> Self {
        Self { username, content, reply: true, retweet: true }
    }
}

impl fmt::Display for Tweet  {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "from Display impl: {}", self.summarize())
    }
}

pub fn notify<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}

#[allow(dead_code)]
fn some_function<T, U>(t: T, u: T) -> i32 where T: Display + Clone, U: Clone + Debug{
    15
}

fn main() {
    let t_1 = Tweet::new(String::from("SomeUsername"), String::from("Some content random bla bla bla"));
    println!("{}", t_1.summarize());
    println!("--------------");
    println!("{}", t_1);

    let a_1 = NewsArticle{
        headline: String::from("abcd"),
        location: String::from("Somewhere"),
        author: String::from("Someone"),
        content: String::from("Someone random text bla bla bla 2 3 4 56"),
    };

    println!("{:#?}", a_1);
    println!("{}", a_1.summarize_2(String::from("Default implementaion")));
    notify(a_1);
}
