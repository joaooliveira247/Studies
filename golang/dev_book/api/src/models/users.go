package models

import "time"

type User struct {
	ID uint `json:"id,omitempty"`
	Name string `json:"name,omitempty"`
	UserName string `json:"user_name,omitempty"`
	Email string `json:"email,omitempty"`
	Password string `json:"password,omitempty"`
	CreatedAt time.Time `json:"created_at,omitempty"`
}