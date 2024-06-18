package main

import "fmt"

func sum(a int8, b int8) int8 {
	return a + b
}

func calc(a, b int8) (int8, int8) {
	sum := a + b
	sub := a - b
	return sum, sub
}

func main() {
	sumNums := sum(12, 6)
	fmt.Println(sumNums)

	var mult = func (a int8, b int8) int8 {
		return a * b
	}

	fmt.Println(mult(4, 5))
	fmt.Println(calc(10, 7))
}