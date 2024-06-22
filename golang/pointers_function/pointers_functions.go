package main

import "fmt"

func invert(n *int) {
	*n = *n * -1
}

func main() {
	num := 20
	invert(&num)
	fmt.Println(num)
}
