package models

import "time"

type Posts struct {
	ID uint64 `json:"id,omitempty"`
	Title string `json:"title,omitempty"`
	Content uint64 `json:"content,omitempty"`
	AuthorID uint64 `json:"author_id,omitempty"`
	AuthorUserName uint64 `json:"author_user_name,omitempty"`
	Likes uint64 `json:"likes"`
	CreatedAt time.Time `json:"created_at,omitempty"`
}