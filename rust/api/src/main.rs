use axum::{Json, http::StatusCode};
use serde::{Deserialize, Serialize};
use tower_http::trace::TraceLayer;
use utoipa::{OpenApi, ToSchema};
use utoipa_axum::{router::OpenApiRouter, routes};
use utoipa_swagger_ui::SwaggerUi;

#[derive(OpenApi)]
#[openapi(
    paths(root, create_user),
    components(schemas(User, CreateUser)),
    tags((name = "Test Api", description = "My first rust api documentation"))
)]
struct ApiDoc;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    /*
    let app = Router::new()
        .route("/", get(root))
        .route("/user/", post(create_user))
        .layer(TraceLayer::new_for_http());

    */

    let (router, api) = OpenApiRouter::with_openapi(ApiDoc::openapi())
        .routes(routes!(root, create_user))
        .split_for_parts();

    let app = router
        .merge(SwaggerUi::new("/api/docs").url("/api-docs/openapi.json", api))
        .layer(TraceLayer::new_for_http());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    println!("🚀 Swagger: http://localhost:3000/api/docs");
    axum::serve(listener, app).await.unwrap();
}

#[utoipa::path(get, path = "/", responses((status = 200, description = "Hello funcion", body = &'static str)))]
async fn root() -> &'static str {
    "Hello, Axum!"
}

#[utoipa::path(post, path = "/user/", request_body = CreateUser,responses((status = 201, description = "Create a user", body = User )), )]
async fn create_user(Json(payload): Json<CreateUser>) -> (StatusCode, Json<User>) {
    let user = User {
        id: 1137,
        username: payload.username,
    };

    (StatusCode::CREATED, Json(user))
}

#[derive(Deserialize, Serialize, ToSchema)]
struct CreateUser {
    username: String,
}

#[derive(Serialize, Deserialize, ToSchema)]
struct User {
    id: u64,
    username: String,
}
