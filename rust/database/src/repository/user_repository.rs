use crate::models::{Book, BookActiveModel, BookModel};
use anyhow::Ok;
use async_trait::async_trait;
use sea_orm::{ActiveModelTrait, ActiveValue::Set, DatabaseConnection, EntityTrait};

#[async_trait]
pub trait BookRepository: Send + Sync {
    async fn create(
        &self,
        title: &str,
        author: &str,
        publication_year: i32,
    ) -> Result<BookModel, anyhow::Error>;

    async fn get_all(&self) -> Result<Vec<BookModel>, anyhow::Error>;
}

pub struct BookRepositoryImpl {
    db: DatabaseConnection,
}

impl BookRepositoryImpl {
    pub fn new(db: DatabaseConnection) -> Self {
        Self { db }
    }
}

#[async_trait]
impl BookRepository for BookRepositoryImpl {
    async fn create(
        &self,
        title: &str,
        author: &str,
        publication_year: i32,
    ) -> anyhow::Result<BookModel> {
        let new_book = BookActiveModel {
            title: Set(title.to_string()),
            author: Set(author.to_string()),
            publication_year: Set(publication_year),
            ..Default::default()
        };

        let inserted = new_book.insert(&self.db).await?;

        Ok(inserted)
    }

    async fn get_all(&self) -> Result<Vec<BookModel>, anyhow::Error> {
        let results = Book::find().all(&self.db).await?;

        Ok(results)
    }
}
