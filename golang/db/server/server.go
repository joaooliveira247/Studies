package server

import (
	"db/database"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type User struct {
	Id    uint32 `json:"id"`
	Name  string `json:name`
	Age   uint32 `json:age`
	Email string `json: email`
}

func CreateUser(w http.ResponseWriter, r *http.Request) {
	requestBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		w.Write([]byte("Error when read body request."))
		return
	}

	var user User

	if err = json.Unmarshal(requestBody, &user); err != nil {
		w.Write([]byte("Error when convert request body in valid user."))
	}

	stringConnection := "user:passwd@tcp(localhost:3306)/mydatabase?charset=utf8&parseTime=True&loc=Local"
	db, err := database.ConnectDB(stringConnection)
	if err != nil {
		w.Write([]byte("Error when try connect with database."))
		return
	}

	defer db.Close()

	statement, err := db.Prepare(
		"INSERT INTO user (name, age, email) VALUES (?, ?, ?);",
	)
	if err != nil {
		w.Write([]byte("Error when try create statement."))
		return
	}
	defer statement.Close()

	insert, err := statement.Exec(user.Name, user.Age, user.Email)

	if err != nil {
		w.Write([]byte("Error when try exec statement."))
		return
	}

	idInsert, err := insert.LastInsertId()

	if err != nil {
		w.Write([]byte("Error when try get id statement."))
		return
	}

	w.WriteHeader(http.StatusCreated)
	w.Write([]byte(fmt.Sprintf("success! user id: %d", idInsert)))
}
