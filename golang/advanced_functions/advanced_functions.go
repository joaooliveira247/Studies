package main

import "fmt"

func mathCalc(a int, b int) (sum int, sub int) {
	sum = a + b
	sub = a - b
	return
}

func main() {
	fmt.Println(mathCalc(3, 2))	
}