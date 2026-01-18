use database::{config, db, state::AppState};

#[tokio::main]
async fn main() {
    config::load_env();

    let db = db::connect().await;

    let state = AppState::new(db.clone());

    /*
    let saved = state
        .book_repo
        .create("It", "Stephen King", 1986)
        .await
        .expect("Error when try create a book.");

    println!("Created book: {:?}", saved)
    */

    let books = state
        .book_repo
        .get_all()
        .await
        .expect("Error when try find books");

    println!("Books: {:?}", books)
}
