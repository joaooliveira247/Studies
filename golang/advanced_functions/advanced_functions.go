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

func main() {
	// closure
	func (text string) {
		fmt.Println(text)
	}("Hello closure")
}
