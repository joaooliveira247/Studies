package main

import "fmt"

func functionOne() {
	fmt.Println("Running function one")
}

func functionsTwo() {
	fmt.Println("Running function two")
}

func main() {
	fmt.Println("Running main")
	defer functionsTwo()
	functionOne()
}