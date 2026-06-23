use sea_orm::{
    ActiveModelTrait, ActiveValue::Set, ColumnTrait, Database, DbErr, EntityTrait, QueryFilter,
};
use seaorm_examples::{
    CustomerEntity, CustomerModel,
    models::{self, customer},
};

#[tokio::main]
async fn main() -> Result<(), DbErr> {
    let database_url = "mysql://user:passwd@localhost:3306/customers";

    let db = Database::connect(database_url).await?;

    // insert
    // let new_customer = models::customer::ActiveModel {
    //     name: Set("Julia Costa".to_owned()),
    //     phone: Set("+55 11 91234-5678".to_owned()),
    //     ..Default::default()
    // };

    // let inserted_customer: CustomerModel = new_customer.insert(&db).await?;

    // println!("Customer inserted ! ID: {}", inserted_customer.id);
    //
    // Read All
    // let all_customers: Vec<CustomerModel> = CustomerEntity::find().all(&db).await?;

    // println!("{:?}", all_customers);

    // Update
    // if let Some(customer_update) = CustomerEntity::find_by_id(3).one(&db).await? {
    //     let mut am: models::customer::ActiveModel = customer_update.into();

    //     am.name = Set("Carlos Eduardo".to_owned());

    //     let customer_updated = am.update(&db).await?;
    //     println!("{:?}", customer_updated);
    // }

    // read filter
    // let search_customer = CustomerEntity::find()
    //     .filter(customer::Column::Id.eq(3))
    //     .one(&db)
    //     .await?;

    // if let Some(c) = search_customer {
    //     println!("{:?}", c);
    // }
    //
    let result_delete = CustomerEntity::delete_by_id(4).exec(&db).await?;

    println!("rows deleted {}", result_delete.rows_affected);

    Ok(())
}
