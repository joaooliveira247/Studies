package models

import (
	"errors"
	"time"
)

type User struct {
	ID        uint      `json:"id,omitempty"`
	Name      string    `json:"name,omitempty"`
	UserName  string    `json:"user_name,omitempty"`
	Email     string    `json:"email,omitempty"`
	Password  string    `json:"password,omitempty"`
	CreatedAt time.Time `json:"created_at,omitempty"`
}

func (u *User) validate() error {

	if u.Name == "" {
		return errors.New("Field Cannot be empty.")
	}
	if u.UserName == "" {
		return errors.New("Field Cannot be empty.")
	}
	if u.Email == "" {
		return errors.New("Field Cannot be empty.")
	}
	if u.Password == "" {
		return errors.New("Field Cannot be empty.")
	}

	return nil
}
