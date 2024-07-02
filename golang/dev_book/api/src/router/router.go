package router

import "github.com/gorilla/mux"

func GenRouter() *mux.Router {
	return mux.NewRouter()
}