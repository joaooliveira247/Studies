package http

import (
	"html/template"
	"log"
	"net/http"
)

var templates *template.Template

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

type User struct {
	Name  string
	Email string
}

func HTMLHome(w http.ResponseWriter, r *http.Request) {
	user := User{
		"SomeName", "some@email.com",
	}
	templates.ExecuteTemplate(w, "example.html", user)
}

func HTMLReturn() {
	templates = template.Must(template.ParseGlob("./http/*.html"))

	http.HandleFunc("/home", HTMLHome)

	log.Fatal(http.ListenAndServe(":5000", nil))
}
