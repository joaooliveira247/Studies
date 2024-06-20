package main

import "fmt"

func main() {
	user := map[string]string{
		"name":     "John",
		"lastname": "Doe",
	}
	fmt.Println(user, user["name"], user["lastname"])
	delete(user, "lastname")
	fmt.Println(user)
	user["college"] = "M.I.T"
	fmt.Println(user)
}
