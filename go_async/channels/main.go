package main

import "fmt"

func worker(ch chan string) {
	ch <- "Hello from goroutine"
}

func main() {
	ch := make(chan string)

	go worker(ch)

	msg := <-ch

	fmt.Println(msg)
	close(ch)
}
