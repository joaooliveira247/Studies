package db

import (
	"database/sql"
	"log"
)


const userTable = `
CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(255),
	age INT,
	email VARCHAR(255),
	password VARCHAR(255),
	created_at DATE,
	PRIMARY KEY (id)
);
`