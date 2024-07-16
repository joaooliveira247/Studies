package models

import (
	"errors"
	"strings"
	"time"
)

type Posts struct {
	ID             uint64    `json:"id,omitempty"`
	Title          string    `json:"title,omitempty"`
	Content        string    `json:"content,omitempty"`
	AuthorID       uint64    `json:"author_id,omitempty"`
	AuthorUserName uint64    `json:"author_user_name,omitempty"`
	Likes          uint64    `json:"likes"`
	CreatedAt      time.Time `json:"created_at,omitempty"`
}

func (post *Posts) format() {
	post.Title = strings.TrimSpace(post.Title)
	post.Content = strings.TrimSpace(post.Content)
}

func (post *Posts) validate() error {
	if post.Title == "" {
		return errors.New("field cannot be empty")
	}
	if post.Content == "" {
		return errors.New("field cannot be empty")
	}
	return nil
}
