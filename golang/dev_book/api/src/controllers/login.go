package controllers

import (
	"api/src/db"
	"api/src/models"
	"api/src/repositories"
	"api/src/token"
	"api/src/response"
	"api/src/security"
	"encoding/json"
	"io/ioutil"
	"net/http"
)

func Login(w http.ResponseWriter, r *http.Request) {
	requestBody, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
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
	defer db.Close()

	repository := repositories.NewUserRepository(db)

	userInDB, err := repository.SearchByEmail(user.Email)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	if err = security.HashVerify(user.Password, userInDB.Password); err != nil {
		response.Erro(w, http.StatusUnauthorized, err)
		return
	}

	token, _ := token.CreateToken(uint64(userInDB.ID))
	w.Write([]byte(token))
}
