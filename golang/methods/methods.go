package main

import "fmt"

type User struct {
	name string
	age  uint
}

func (u User) save(conn string) {
	ret_string := fmt.Sprintf("%s %d save in: %s", u.name, u.age, conn)
	fmt.Println(ret_string)
}

func (u *User) incrementAge() {
	u.age++
}

func main() {
	user1 := User{"John", 21}
	user1.save("postgresql://user:passwd@localhsot:5432/db")
	user1.incrementAge()
	fmt.Println(user1.age)
}
