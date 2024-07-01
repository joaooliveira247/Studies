package main

import (
	"db/database"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	stringConnection := "user:passwd@tcp(localhost:3306)/mydatabase?charset=utf8&parseTime=True&loc=Local"
	db := database.ConnectDB(stringConnection)
	defer db.Close()
	router := mux.NewRouter()
	// creteTable(db)
	log.Fatal(http.ListenAndServe(":5000", router))
}
