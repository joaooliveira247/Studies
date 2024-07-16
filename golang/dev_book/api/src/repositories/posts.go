package repositories

import (
	"api/src/models"
	"database/sql"
)

type Posts struct {
	db *sql.DB
}

func NewPostsRepository(db *sql.DB) *Posts {
	return &Posts{db}
}

func (p Posts) CreatePost(post models.Posts) (uint64, error) {
	statement, err := p.db.Prepare(
		`INSERT INTO 
			posts (title, content, author_id)
		VALUSE (?, ?, ?);
		`,
	)
	if err != nil {
		return 0, err
	}
	defer statement.Close()

	result, err := statement.Exec(post.Title, post.Content, post.AuthorID)
	if err != nil {
		return 0, err
	}
	lastInsertedID, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}
	return uint64(lastInsertedID), nil
}

func (p Posts) GetPostByID(postID uint64) (models.Posts, error) {
	lines, err := p.db.Query(
		`
		SELECT
			p.*, u.username 
		FROM 
			posts p 
		INNER JOIN 
			users u 
		ON 
			p.author_id = u.id
		WHERE p.id = ?;
		`, postID,
	)
	if err != nil {
		return models.Posts{}, err
	}
	defer lines.Close()

	var post models.Posts

	if err = lines.Scan(
		&post.ID,
		&post.Title,
		&post.Content,
		&post.AuthorID,
		&post.Likes,
		&post.CreatedAt,
		&post.AuthorUserName,
	); err != nil {
		return models.Posts{}, err
	}

	return post, nil
}
