use dotenv::dotenv;
use mysql::{Opts, Pool, PooledConn};
use std::env;

pub fn get_connection() -> Result<PooledConn, mysql::Error> {
    dotenv().ok();

    let database_url = env::var("DATABASE_URL").expect("Error when tyr load DATABASE_URL from env");

    let opts = Opts::from_url(&database_url)?;
    let pool = Pool::new(opts)?;
    let conn = pool.get_conn()?;

    Ok(conn)
}
