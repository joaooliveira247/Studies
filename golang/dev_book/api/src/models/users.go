package models

import (
	"errors"
	"strings"
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

func (u *User) Prepare(process string) error {
	if err := u.validate(process); err != nil {
		return err
	}

	u.format()
	return nil
}

func (u *User) validate(process string) error {

	if u.Name == "" {
		return errors.New("field cannot be empty")
	}
	if u.UserName == "" {
		return errors.New("field cannot be empty")
	}
	if u.Email == "" {
		return errors.New("field cannot be empty")
	}
	if process == "create" && u.Password == "" {
		return errors.New("field cannot be empty")
	}

	return nil
}

func (u *User) format() {
	u.Name = strings.TrimSpace(u.Name)
	u.UserName = strings.TrimSpace(u.UserName)
	u.Email = strings.TrimSpace(u.Email)
}
