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

func (p Posts) SearchPosts(userID uint64) ([]models.Posts, error) {
	lines, err := p.db.Query(
		`
		SELECT DISTINCT 
			p.*, u.user_name 
		FROM 
			posts p
		INNER JOIN
			users u
		ON
			u.id = p.author_id
		INNER JOIN
			followers f
		ON
			p.author_id = f.users_id
		WHERE
			u.id = ? OR s.follower_id = ?;
		`, userID, userID,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var posts []models.Posts

	for lines.Next() {
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
			return nil, err
		}
		posts = append(posts, post)
	}

	return posts, nil

}

func (p Posts) UpdatePost(postID uint64, post models.Posts) error {
	statement, err := p.db.Prepare(
		`UPDATE posts SET title = ?, content = ? WHERE id = ?;`,
	)
	if err != nil {
		return err
	}
	defer statement.Close()

	if _, err = statement.Exec(post.Title, post.Content, postID); err != nil {
		return err
	}
	return nil
}

func (p Posts) DeletePost(postID uint64) error {
	statement, err := p.db.Prepare(
		`DELETE FROM posts WHERE id = ?;`,
	)
	if err != nil {
		return err
	}
	defer statement.Close()

	if _, err = statement.Exec(postID); err != nil {
		return err
	}
	return nil
}

func (p Posts) GetUserPosts(userID uint64) ([]models.Posts, error) {
	lines, err := p.db.Query(
		`
		SELECT
			p.*, u.user_name 
		FROM 
			posts p
		INNER JOIN
			users u
		ON
			p.author_id = u.id
		WHERE
			p.id = ?;
		`,
		userID,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var posts []models.Posts

	for lines.Next() {
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
			return nil, err
		}
		posts = append(posts, post)
	}

	return posts, nil
}
