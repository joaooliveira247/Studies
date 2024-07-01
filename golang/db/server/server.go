package server

import (
	"db/database"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
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

// Get user by id
func GetUserById(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)

	ID, err := strconv.ParseUint(params["id"], 10, 32)

	if err != nil {
		w.Write([]byte(fmt.Sprintf("%s value is not valid.", params["id"])))
		return
	}

	db, err := database.ConnectDB(DBStringConnection)

	if err != nil {
		w.Write([]byte("Error when try connect with database."))
		return
	}

	defer db.Close()

	line, err := db.Query("SELECT * FROM user WHERE id = ?;", ID)

	if err != nil {
		w.Write([]byte("Error when try get data from database."))
		return
	}

	var user User

	if line.Next() {
		if err := line.Scan(&user.Id, &user.Name, &user.Age, &user.Email); err != nil {
			w.Write([]byte("Error when try parser from database."))
			return
		}
	}

	w.WriteHeader(http.StatusOK)
	if err := json.NewEncoder(w).Encode(user); err != nil {
		w.Write([]byte("Error when try parser to JSON."))
		return
	}
}

// Update an user
func UpdateUser(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)

	ID, err := strconv.ParseUint(params["id"], 10, 32)
	if err != nil {
		w.Write([]byte(fmt.Sprintf("%s value is not valid.", params["id"])))
		return
	}

	requestBody, err := ioutil.ReadAll(r.Body)

	if err != nil {
		w.Write([]byte("Error when read body request."))
		return
	}

	var user User

	if err := json.Unmarshal(requestBody, &user); err != nil {
		w.Write([]byte("Error when try parser json."))
		return
	}

	db, err := database.ConnectDB(DBStringConnection)

	if err != nil {
		w.Write([]byte("Error when try connect to database."))
	}

	defer db.Close()

	statement, err := db.Prepare(
		"UPDATE user SET name = ?, age = ?, email = ? WHERE id = ?",
	)
	if err != nil {
		w.Write([]byte("Error when try create statement."))
	}

	defer statement.Close()

	if _, err := statement.Exec(user.Name, user.Age, user.Email, ID); err != nil {
		w.Write([]byte("Error when try update user."))
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

// Delete user
func DeleteUser(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)

	ID, err := strconv.ParseUint(params["id"], 10, 32)

	if err != nil {
		w.Write([]byte(fmt.Sprintf("%s value is not valid.", params["id"])))
		return
	}

	db, err := database.ConnectDB(DBStringConnection)

	if err != nil {
		w.Write([]byte("Error when try connect to database."))
	}

	defer db.Close()

	statement, err := db.Prepare("DELETE FROM user WHERE id = ?;")

	if err != nil {
		w.Write([]byte("Error when try create statement."))
		return
	}

	defer statement.Close()

	if _, err := statement.Exec(ID); err != nil {
		w.Write([]byte("Error when try delete user."))
		return
	}

	w.WriteHeader(http.StatusNoContent)
}
