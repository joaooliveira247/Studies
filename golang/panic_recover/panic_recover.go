package main

import "fmt"

func backAction() {
	if r := recover(); r != nil {
		fmt.Println("func recovery")
	}
}

func approved(n1, n2 float64) bool {
	defer backAction()
	mean := (n1 + n2) / 2

	if mean > 6 {
		return true
	} else if mean < 6 {
		return false
	}
	panic("Mean 6")
}

func main() {
	fmt.Println(approved(6, 6))
	fmt.Println("after exec")
}
