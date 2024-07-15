package db

import (
	"log"
)

const userTable = `
CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(255) NOT NULL,
	user_name VARCHAR(255) NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	created_at DATE default current_timestamp(),
	PRIMARY KEY (id)
);
`

const followerTable = `
CREATE TABLE IF NOT EXISTS followers(
	users_id INT NOT NULL,
	FOREIGN KEY (users_id)
	REFERENCES users(id)
	ON DELETE CASCADE,
	follower_id INT NOT NULL,
	FOREIGN KEY (follower_id)
	REFERENCES users(id)
	ON DELETE CASCADE,
	PRIMARY KEY (users_id, follower_id)
);
`

const postsTable = `
CREATE TABLE IF NOT EXISTS posts(
	id INT AUTOINCREMENT NOT NULL,
	title VARCHAR(50) NOT NULL,
	content TEXT NOT NULL,
	author_id INT NOT NULL
	FOREIGN KEY (author_id)
	REFERENCES users(id)
	ON DELETE CASCADE,
	likes INT DEFAULT 0,
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
		userTable, followerTable, postsTable,
	}
	for _, table := range tables {
		if _, err := conn.Query(table); err != nil {
			log.Fatal(err)
		}
	}
}
