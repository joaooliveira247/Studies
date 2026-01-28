use axum::{Router, routing::get};
use tower_http::trace::TraceLayer;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let app = Router::new()
        .route("/", get(root))
        .layer(TraceLayer::new_for_http());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();

    tracing::info!("🚀 Server running on http://localhost:3000");

    axum::serve(listener, app).await.unwrap()
}

async fn root() -> &'static str {
    "Hello, Axum!"
}
