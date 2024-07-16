package repositories

import "database/sql"

type Posts struct {
	db *sql.DB
}

func NewPostsRepository(db *sql.DB) *Posts {
	return &Posts{db}
}