use sea_orm::DatabaseConnection;
use std::sync::Arc;

use crate::repository::{BookRepository, BookRepositoryImpl};

#[derive(Clone)]
pub struct AppState {
    pub book_repo: Arc<dyn BookRepository>,
}

impl AppState {
    pub fn new(db: DatabaseConnection) -> Self {
        let repo = Arc::new(BookRepositoryImpl::new(db));
        Self { book_repo: repo }
    }
}
