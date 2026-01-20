use crate::models::{Book, BookActiveModel, BookModel};
use anyhow::Ok;
use async_trait::async_trait;
use sea_orm::{ActiveModelTrait, ActiveValue::Set, DatabaseConnection, EntityTrait};
use uuid::Uuid;

#[async_trait]
pub trait BookRepository: Send + Sync {
    async fn create(
        &self,
        title: &str,
        author: &str,
        publication_year: i32,
    ) -> Result<BookModel, anyhow::Error>;

    async fn get_all(&self) -> Result<Vec<BookModel>, anyhow::Error>;

    async fn get_by_id(&self, id: Uuid) -> Result<Option<BookModel>, anyhow::Error>;

    async fn update(
        &self,
        id: Uuid,
        title: Option<&str>,
        author: Option<&str>,
        publication_year: Option<i32>,
    ) -> Result<(), anyhow::Error>;
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

    async fn get_by_id(&self, id: Uuid) -> Result<Option<BookModel>, anyhow::Error> {
        let result = Book::find_by_id(id).one(&self.db).await?;

        Ok(result)
    }
}
