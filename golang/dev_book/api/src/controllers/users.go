package controllers

import (
	"api/src/db"
	"api/src/models"
	"api/src/repositories"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func CreateUser(w http.ResponseWriter, r *http.Request) {
	requestBody, err := ioutil.ReadAll(r.Body)

	if err != nil {
		log.Fatal(err)
	}

	var user models.User

	if err = json.Unmarshal(requestBody, &user); err != nil {
		log.Fatal(err)
	}

	db, err := db.GetConnection()

	if err != nil {
		log.Fatal(err)
	}

	repository := repositories.NewUserRepository(db)
	userID, err := repository.Create(user)
	if err != nil {
		log.Fatal(err)
	}
	w.Write([]byte(fmt.Sprintf("%d", userID)))
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
