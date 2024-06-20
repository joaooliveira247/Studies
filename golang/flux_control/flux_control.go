package main

import "fmt"

func main() {
	num := 10

	if num > 15 {
		fmt.Println("GT 15")
	} else {
		fmt.Println("LT 15")
	}

	// if init
	if anotherOne := num; anotherOne > 0 {
		fmt.Println("GT 0")
	} else if anotherOne < -10 {
		fmt.Println("LT -10")
	} else {
		fmt.Println("LT 0")
	}
}
