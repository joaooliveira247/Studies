package main

import "fmt"

func mathCalc(a int, b int) (sum int, sub int) {
	sum = a + b
	sub = a - b
	return
}

func variadicSumFunction(n ...int) int {
	total := 0
	for _, num := range n {
		total += num
	}
	return total
}

func recursiveFibonnaci(pos uint) uint {
	if pos <= 1 {
		return pos
	}
	return recursiveFibonnaci(pos-2) + recursiveFibonnaci(pos-1)
}

func main() {
	// closure
	func(text string) {
		fmt.Println(text)
	}("Hello closure")

	fmt.Println(recursiveFibonnaci(10))
}
