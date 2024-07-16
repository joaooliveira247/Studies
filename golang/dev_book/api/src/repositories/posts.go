package repositories

import "database/sql"

type Posts struct {
	db *sql.DB
}