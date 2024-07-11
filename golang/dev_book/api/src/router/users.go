package router

import (
	"api/src/controllers"
	"net/http"
)

var userRoutes = []Route{
	{
		URI:     "/users",
		Method:  http.MethodPost,
		Func:    controllers.CreateUser,
		AuthReq: false,
	},
	{
		URI:     "/users",
		Method:  http.MethodGet,
		Func:    controllers.GetUsers,
		AuthReq: true,
	},
	{
		URI:     "/users/{userID}",
		Method:  http.MethodGet,
		Func:    controllers.GetUserbyId,
		AuthReq: true,
	},
	{
		URI:     "/users/{userID}",
		Method:  http.MethodPut,
		Func:    controllers.UpdateUser,
		AuthReq: true,
	},
	{
		URI:     "/users/{userID}",
		Method:  http.MethodDelete,
		Func:    controllers.DeleteUser,
		AuthReq: false,
	},
}
