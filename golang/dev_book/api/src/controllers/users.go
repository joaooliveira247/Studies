package controllers

import (
	"api/src/db"
	"api/src/models"
	"api/src/repositories"
	"api/src/response"
	"encoding/json"
	"io/ioutil"
	"net/http"
)

func CreateUser(w http.ResponseWriter, r *http.Request) {
	requestBody, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var user models.User

	if err = json.Unmarshal(requestBody, &user); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	db, err := db.GetConnection()

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	repository := repositories.NewUserRepository(db)
	userID, err := repository.Create(user)
	user.ID = uint(userID)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	response.JSON(w, http.StatusCreated, user)
}

func GetUsers(w http.ResponseWriter, t *http.Request) {
	w.Write([]byte("Not implemented"))
}

func GetUserbyId(w http.ResponseWriter, t *http.Request) {
	w.Write([]byte("Not implemented"))
}

func UpdateUser(w http.ResponseWriter, t *http.Request) {
	w.Write([]byte("Not implemented"))
}

func DeleteUser(w http.ResponseWriter, t *http.Request) {
	w.Write([]byte("Not implemented"))
}
