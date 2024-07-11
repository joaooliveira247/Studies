package middlewares

import (
	"api/src/response"
	"api/src/token"
	"log"
	"net/http"
)

func Logger(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Printf("\n %s %s %s", r.Method, r.RequestURI, r.Host)
	}
}

func Auth(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if err := token.TokenValidation(r); err != nil {
			response.Erro(w, http.StatusUnauthorized, err)
			return
		}
		next(w, r)
	}
}
