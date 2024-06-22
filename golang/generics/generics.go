package main

import "fmt"

type Any interface {}

func generics(value Any) {
	fmt.Println(value)
}

func main() {
	generics(1)
	generics("Hello")
	generics(true)
}	