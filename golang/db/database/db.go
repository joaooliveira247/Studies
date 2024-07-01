package database

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func check(err error) {
	log.Fatal(err)
}

func ConnectDB(stringConnection string) (*sql.DB, error) {
	db, err := sql.Open("mysql", stringConnection)

	if err != nil {
		return nil, err
	}

	if err = db.Ping(); err != nil {
		return nil, err
	}

	fmt.Printf("Connected in %s", stringConnection)

	return db, nil
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
