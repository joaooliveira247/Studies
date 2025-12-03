use std::env;
use std::fs::File;
use std::io::{Error, prelude::*};

type StrSlice<'a> = &'a str;

pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        if !(args.len() == 3) {
            return Err("not enough arguments");
        }
        let (query, filename) = (args[1].clone(), args[2].clone());

        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();
        
        Ok(Config {
            query,
            filename,
            case_sensitive,
        })
    }
}

pub fn search<'a>(query: &str, contents: StrSlice<'a>) -> Vec<StrSlice<'a>> {
    let mut results = Vec::new();
    for line in contents.lines() {
        if line.contains(&query) {
            results.push(line);
        }
    }
    results
}

pub fn search_case_insensitive<'a>(query: &str, contents: StrSlice<'a>) -> Vec<StrSlice<'a>> {
    let mut results = Vec::new();
    for line in contents.lines() {
        if line.to_lowercase().contains(&query.to_lowercase()) {
            results.push(line);
        }
    }
    results
}

pub fn run(config: Config) -> Result<(), Box<Error>> {
    let mut f = File::open(&config.filename)?;

    let mut contents = String::new();

    f.read_to_string(&mut contents)?;

    let results = if config.case_sensitive {
        search(&config.query, &contents)
    } else {
        search_case_insensitive(&config.query, &contents)
    };

    for line in results {
        println!("{}", line)
    }
    Ok(())
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(vec!["safe, fast, productive."], search(query, contents))
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        )
    }
}
