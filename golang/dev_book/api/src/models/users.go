package models

import (
	"api/src/security"
	"errors"
	"strings"
	"time"

	"github.com/badoux/checkmail"
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

	if err := u.format(process); err != nil {
		return err
	}
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
	if err := checkmail.ValidateFormat(u.Email); err != nil {
		return errors.New("email is not valid")
	}

	if process == "create" && u.Password == "" {
		return errors.New("field cannot be empty")
	}

	return nil
}

func (u *User) format(process string) error {
	u.Name = strings.TrimSpace(u.Name)
	u.UserName = strings.TrimSpace(u.UserName)
	u.Email = strings.TrimSpace(u.Email)

	if process == "create" {
		hashPasswd, err := security.Hash(u.Password)
		if err != nil {
			return err
		}
		u.Password = string(hashPasswd)
	}
	return nil
}
