use crate::models::{Book, BookActiveModel, BookModel};
use anyhow::Ok;
use async_trait::async_trait;
use sea_orm::{ActiveModelTrait, ActiveValue::Set, DatabaseConnection, EntityTrait, ModelTrait};
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

    async fn delete(&self, id: Uuid) -> Result<(), anyhow::Error>;
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

    async fn update(
        &self,
        id: Uuid,
        title: Option<&str>,
        author: Option<&str>,
        publication_year: Option<i32>,
    ) -> Result<(), anyhow::Error> {
        let mut result: BookActiveModel = Book::find_by_id(id).one(&self.db).await?.unwrap().into();

        if let Some(t) = title {
            result.title = Set(t.to_string());
        }

        if let Some(a) = author {
            result.author = Set(a.to_string());
        }

        if let Some(p) = publication_year {
            result.publication_year = Set(p);
        }

        result.update(&self.db).await?;
        Ok(())
    }

    async fn delete(&self, id: Uuid) -> Result<(), anyhow::Error> {
        let result = Book::delete_by_id(id).exec(&self.db).await?;

        println!("{:?}", result);

        if result.rows_affected == 0 {
            Err(anyhow::anyhow!("Book not found"))
        } else {
            Ok(())
        }
    }
}
