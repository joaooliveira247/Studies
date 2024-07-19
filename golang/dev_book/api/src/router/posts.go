package router

import (
	"api/src/controllers"
	"net/http"
)

var postsRouters = []Route{
	{
		URI: "/posts/",
		Method: http.MethodPost,
		Func: controllers.CreatePost,
		AuthReq: true,
	},
	{
		URI: "/posts/",
		Method: http.MethodGet,
		Func: controllers.GetPosts,
		AuthReq: true,
	},
	{
		URI: "/posts/{postID}",
		Method: http.MethodGet,
		Func: controllers.GetPostByID,
		AuthReq: true,
	},
	{
		URI: "/posts/{postID}",
		Method: http.MethodPut,
		Func: controllers.UpdatePost,
		AuthReq: true,
	},
	{
		URI: "/posts/{postID}",
		Method: http.MethodDelete,
		Func: controllers.DeletePost,
		AuthReq: true,
	},
	{
		URI: "/users/{userID}/posts",
		Method: http.MethodGet,
		Func: controllers.GetUserPosts,
		AuthReq: true,
	},
	{
		URI: "/posts/{postID}/like",
		Method: http.MethodPost,
		Func: controllers.LikePost,
		AuthReq: true,
	},
}