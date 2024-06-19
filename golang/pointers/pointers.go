package main

import "fmt"

func main() {
	var val1 int = 10
	var val2 int = val1

	fmt.Println(val1, val2)

	val1++

	fmt.Println(val1, val2)

	// pointers
	var val3 int
	var pointer *int

	val3 = 100
	//& = ref
	pointer = &val3

	// * = deref
	fmt.Println(val3, pointer, *pointer)

}
