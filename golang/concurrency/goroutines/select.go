package goroutines

import (
	"fmt"
	"time"
)

func Select() {
	ch1, ch2 := make(chan string), make(chan string)

	go func() {
		for {
			time.Sleep(time.Millisecond * 500)
			ch1 <- "Channel 1"
		}
	}()
	go func() {
		for {
			time.Sleep(time.Second * 2)
			ch2 <- "Channel 2"
		}
	}()

	for {
		select {
		case msg1 := <-ch1:
			fmt.Println(msg1)
		case msg2 := <-ch2:
			fmt.Println(msg2)
		}
	}
}
