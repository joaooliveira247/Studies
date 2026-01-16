use crate::config;
use sea_orm::{Database, DatabaseConnection};

pub async fn connect() -> DatabaseConnection {
    config::load_env();
    let url = config::database_url();

    Database::connect(url).await.expect("Failed to connect DB")
}
