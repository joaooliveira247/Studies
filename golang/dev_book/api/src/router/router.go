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
	r := mux.NewRouter()
	return Configure(r)
}

func Configure(r *mux.Router) *mux.Router {
	routes := userRoutes

	for _, route := range routes {
		r.HandleFunc(route.URI, route.Func).Methods(route.Method)
	}

	return r
}
