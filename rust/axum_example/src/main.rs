use axum::{
    Json, Router,
    routing::{get, post},
};
use serde::{Deserialize, Serialize};
use utoipa::{OpenApi, ToSchema};
use utoipa_swagger_ui::SwaggerUi;

#[derive(Serialize, Deserialize, ToSchema, Clone)]
struct Todo {
    id: u32,
    #[schema(example = "Buy milk")]
    title: String,
    completed: bool,
}

#[derive(Deserialize, ToSchema)]
struct CreateTodo {
    #[schema(example = "Buy milk")]
    title: String,
}

#[derive(OpenApi)]
#[openapi(
    paths(
        get_all,
        create_todo
    ),
    components(schemas(Todo, CreateTodo)),
    tags(
        (name = "Todo API", description = "Endpoints to doc Todo app.")
    )
)]
struct ApiDoc;

#[tokio::main]
async fn main() {
    let swagger_ui = SwaggerUi::new("/swagger-ui").url("/api-docs/openapi.json", ApiDoc::openapi());

    let app = Router::new()
        .route("/todo", get(get_all))
        .route("/todo", post(create_todo))
        .merge(swagger_ui); // Mescla o sub-router do Swagger gerado acima

    let listener = tokio::net::TcpListener::bind("127.0.0.1:8000")
        .await
        .unwrap();

    axum::serve(listener, app).await.unwrap();
}

#[utoipa::path(
    get,
    path = "/todo",
    responses(
        (status = 200, description = "List all todo's", body = [Todo] )
    )
)]
async fn get_all() -> Json<Vec<Todo>> {
    let all = vec![
        Todo {
            id: 1,
            title: "Learning Axum".to_string(),
            completed: false,
        },
        Todo {
            id: 1,
            title: "Config Swagger".to_string(),
            completed: true,
        },
    ];
    Json(all)
}

#[utoipa::path(post, path = "/todo", request_body = CreateTodo, responses((status = 201, description = "Task success created", body = Todo)))]
async fn create_todo(Json(payload): Json<CreateTodo>) -> (axum::http::StatusCode, Json<Todo>) {
    let new_todo = Todo {
        id: 3,
        title: payload.title,
        completed: false,
    };
    (axum::http::StatusCode::CREATED, Json(new_todo))
}
