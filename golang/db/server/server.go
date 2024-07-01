package server

import (
	"db/database"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

const DBStringConnection = "user:passwd@tcp(localhost:3306)/mydatabase?charset=utf8&parseTime=True&loc=Local"

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

	db, err := database.ConnectDB(DBStringConnection)
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

// Get all users from db
func GetUsers(w http.ResponseWriter, r *http.Request) {
	db, err := database.ConnectDB(DBStringConnection)

	if err != nil {
		w.Write([]byte("Error when try connect with database."))
		return
	}

	defer db.Close()

	lines, err := db.Query("SELECT * from user;")

	if err != nil {
		w.Write([]byte("Error when try get data from database."))
		return
	}
	defer lines.Close()

	var users []User

	for lines.Next() {
		var user User

		if err := lines.Scan(&user.Id, &user.Name, &user.Age, &user.Email); err != nil {
			w.Write([]byte("Error when try parser from database."))
			return
		}
		users = append(users, user)
	}

	w.WriteHeader(http.StatusOK)

	if err := json.NewEncoder(w).Encode(users); err != nil {
		w.Write([]byte("Error when try parser to JSON."))
			return
	}

}
