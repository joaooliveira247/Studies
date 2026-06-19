use serde::{Deserialize, Serialize};
use uuid::Uuid;

#[derive(Serialize, Deserialize, Debug)]
pub struct Customer {
    pub id: Uuid,
    pub name: String,
    pub phone: String,
}
