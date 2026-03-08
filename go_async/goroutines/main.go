package main

import (
	"fmt"
	"time"
)

func fun(value string) {
	for i := 0; i < 3; i++ {
		fmt.Println(value)
		time.Sleep(1 * time.Millisecond)
	}
}

func funPointer(value *string) {
	for {
		fmt.Println(&value)
		time.Sleep(1 * time.Millisecond)
	}
}

// By default func main run in a Gourotine
func main() {
	fun("Goroutine - 0")

	go fun("Goroutine - 1")

	fx := fun

	go fx("Goroutine - 2")

	go func(value string) {
		fun(value)
	}("Goroutine - 3")

	time.Sleep(5 * time.Millisecond)

	fmt.Println("Done ....")

	a := "Pointer Goroutine"

	go funPointer(&a)
}
