package goroutines

import (
	"fmt"
	"time"
)

func writeMultplexing(text string) <-chan string {
	ch := make(chan string)

	go func() {
		for {
			ch <- fmt.Sprintf("Input value: %s", text)
			time.Sleep(time.Millisecond * 500)
		}
	}()

	return ch
}

func multplex(ch1, ch2 <-chan string) <-chan string {
	exitChannel := make(chan string)

	go func() {
		for {
			select {
			case msg := <-ch1:
				exitChannel <- msg
			case msg := <-ch2:
				exitChannel <- msg
			}
		}
	}()

	return exitChannel
}

func Multplexing() {
	// Join channels
	ch := multplex(writeMultplexing("Hello World!"), writeMultplexing("Hello Go!"))

	for i := 0; i < 10; i++ {
		fmt.Println(<-ch)
	}
}
