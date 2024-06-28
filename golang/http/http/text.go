package http

import (
	"log"
	"net/http"
)

func HomeText(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello http"))
}

func UserText(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Some User"))
}

func TextReturn() {
	http.HandleFunc("/home", HomeText)
	http.HandleFunc("/users", UserText)

	log.Fatal(http.ListenAndServe(":5000", nil))
}
