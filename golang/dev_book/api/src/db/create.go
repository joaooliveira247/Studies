package db

import (
	"log"
)

const userTable = `
CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(255),
	user_name VARCHAR(255),
	email VARCHAR(255),
	password VARCHAR(255),
	created_at DATE default current_timestamp(),
	PRIMARY KEY (id)
);
`

func CreateTables() {
	conn, err := GetConnection()
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	tables := []string{
		userTable,
	}
	for _, table := range tables {
		if _, err := conn.Query(table); err != nil {
			log.Fatal(err)
		}
	}
}
