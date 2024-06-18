package main

import (
	"fmt"
)

const piValue = 3.14

func main() {
	var name string = "John"
	name2 := "Peter"
	fmt.Println(name, name2)

	var (
		val1 int = 1
		val2 int = 2
	)
	fmt.Println(val1, val2)

	val3, val4 := 3, 4
	fmt.Println(val3, val4)

	fullName := fmt.Sprintf("%s %s", name, name2)
	fmt.Println(fullName)
	fmt.Println(piValue)
}