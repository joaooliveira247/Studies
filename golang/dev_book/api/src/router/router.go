package router

import (
	"net/http"

	"github.com/gorilla/mux"
)

type Route struct {
	URI     string
	Method  string
	Func    func(http.ResponseWriter, *http.Request)
	AuthReq bool
}

func GenRouter() *mux.Router {
	return mux.NewRouter()
}
