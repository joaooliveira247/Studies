package router

import (
	"api/src/middlewares"
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
	routes = append(routes, loginRoutes)
	routes = append(routes, postsRouters...)

	for _, route := range routes {

		if route.AuthReq {
			r.HandleFunc(
				route.URI,
				middlewares.Logger(middlewares.Auth(route.Func)),
			).Methods(route.Method)
		} else {
			r.HandleFunc(
				route.URI,
				middlewares.Logger(route.Func)).Methods(route.Method)
		}
	}

	return r
}
