package main

import "fmt"

type City struct {
	name string
}

type User struct {
	name string
	age  uint8
	city City
}

func main() {
	var user1 User
	fmt.Println(user1)
	user1.name = "John"
	user1.age = 18
	fmt.Println(user1)

	user2 := User{"Jane", 21, City{"RJ"}}
	fmt.Println(user2)

	user3 := User{name: "Peter"}
	fmt.Println(user3)
}
