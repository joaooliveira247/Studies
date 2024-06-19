package main

import "fmt"

type Person struct {
	name string
	lastName string
	age uint8
}

type Student struct {
	Person
	college string
	course string
}

func main() {
	p1 := Person{
		"Jane", "Doe", 19,
	}
	fmt.Println(p1)

	s1 := Student{p1, "M.I.T", "Computational Science"}
	fmt.Println(s1)
	fmt.Println(s1.name, s1.lastName)
}