use database::{config, db, state::AppState};
use uuid::uuid;

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

    println!("Created book: {:?}", saved);
    */

    // let books = state
    //     .book_repo
    //     .get_all()
    //     .await
    //     .expect("Error when try find books");

    // println!("Books: {:?}", books)

    /*
    if let Some(book) = state
        .book_repo
        .get_by_id(uuid!("95c431c1-ca73-4fa6-b894-1012d4e263b7"))
        .await
        .expect("Error when try find book")
    {
        println!("Book: {:?}", book)
    } else {
        println!("Book not found")
    }
    */
    /*
    state.book_repo.update(uuid!("80ba8e52-abb5-4153-8f0b-9fb8669f988d"), Some("Carrie"), None, Some(1974)).await.expect("Error when try update book");
    */

    let _ = state
        .book_repo
        .delete(uuid!("da9055cd-8c8b-4cd5-aae9-a677a72e8006"))
        .await
        .expect("Error when try delete book");
}
