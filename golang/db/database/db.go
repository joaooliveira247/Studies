package database

import (
	"database/sql"
	"fmt"
	"log"
	_ "github.com/go-sql-driver/mysql"
)

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func ConnectDB(stringConnection string) *sql.DB {
	db, err := sql.Open("mysql", stringConnection)
	check(err)
	check(db.Ping())
	fmt.Printf("Connected in %s", stringConnection)
	return db

}

func CreteTable(db *sql.DB) {
	tx, err := db.Begin()
	check(err)
	_, err = tx.Exec(
		`
		CREATE TABLE IF NOT EXISTS 
			user(
				id INTEGER AUTO_INCREMENT NOT NULL,
				name VARCHAR(255),
				age INTEGER,
				email VARCHAR(255),
				PRIMARY KEY (id)
				);
				`,
	)
	check(err)
	err = tx.Commit()
	check(err)
}
