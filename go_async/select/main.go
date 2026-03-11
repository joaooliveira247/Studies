package main

import (
	"context"
	"fmt"
	"time"
)

func getValueFromChannel(ch chan<- string, duration time.Duration) {
	time.Sleep(duration)
	ch <- "That's all folks!"
}

// select is a switch to use with channels
func main() {

	ctx, _ := context.WithTimeout(context.Background(), 1*time.Second)

	ch := make(chan string)
	go getValueFromChannel(ch, time.Second*20)

	ch2 := make(chan string)
	go getValueFromChannel(ch2, time.Second*20)

	ch3 := make(chan string)
	go getValueFromChannel(ch3, time.Second*20)

	for {
		select {
		case returnValue := <-ch:
			fmt.Println(returnValue)
		case returnValue := <-ch2:
			fmt.Println(returnValue)
		case returnValue := <-ch3:
			fmt.Println(returnValue)
		case <-ctx.Done():
			fmt.Println("Max time exceded")
		}
	}
}
