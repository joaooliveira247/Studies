package controllers

import (
	"api/src/db"
	"api/src/models"
	"api/src/repositories"
	"api/src/response"
	"api/src/token"
	"encoding/json"
	"io"
	"net/http"
)

func CreatePost(w http.ResponseWriter, r *http.Request) {
	userID, err := token.ExtractUserID(r)
	if err != nil {
		response.Erro(w, http.StatusUnauthorized, err)
		return
	}

	requestBody, err := io.ReadAll(r.Body)
	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var post models.Posts

	if err = json.Unmarshal(requestBody, &post); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	post.AuthorID = userID

	db, err := db.GetConnection()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewPostsRepository(db)

	post.ID, err = repository.CreatePost(post)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	response.JSON(w, http.StatusCreated, post)
}

func GetPosts(w http.ResponseWriter, r *http.Request) {}

func GetPostByID(w http.ResponseWriter, r *http.Request) {}

func UpdatePost(w http.ResponseWriter, r *http.Request) {}

func DeletePost(w http.ResponseWriter, r *http.Request) {}
