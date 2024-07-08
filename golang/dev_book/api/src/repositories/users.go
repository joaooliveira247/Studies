package repositories

import (
	"api/src/models"
	"database/sql"
	"fmt"
)

type Users struct {
	db *sql.DB
}

func NewUserRepository(db *sql.DB) *Users {
	return &Users{db}
}

func (repository Users) Create(user models.User) (uint64, error) {
	statement, err := repository.db.Prepare(
		"INSERT INTO users (name, user_name, email, password) VALUES (?, ?, ?, ?);",
	)
	if err != nil {
		return 0, err
	}
	defer statement.Close()

	result, err := statement.Exec(user.Name, user.UserName, user.Email, user.Password)
	if err != nil {
		return 0, err
	}

	lastInsertedID, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	return uint64(lastInsertedID), nil
}

func (u Users) Search(filter string) ([]models.User, error) {
	filter = fmt.Sprintf("%%%s%%", filter)

	lines, err := u.db.Query(
		`SELECT
			id, name, user_name, email, created_at 
		FROM 
			users 
		WHERE 
		name LIKE ? or user_name LIKE ?;`,
		filter,
		filter,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var users []models.User

	for lines.Next() {
		var user models.User

		if err = lines.Scan(
			&user.ID, &user.Name, &user.UserName, &user.Email, &user.CreatedAt,
		); err != nil {
			return nil, err
		}

		users = append(users, user)
	}

	return users, nil
}
