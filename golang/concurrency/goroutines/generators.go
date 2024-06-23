package goroutines

import (
	"fmt"
	"time"
)

func writeGenerators(text string) <-chan string {
	ch := make(chan string)

	go func() {
		for {
			ch <- fmt.Sprintf("Input value: %s", text)
			time.Sleep(time.Millisecond * 500)
		}
	}()

	return ch
}

func Generators() {
	ch := writeGenerators("Hello World")

	for i := 0; i < 10; i++ {
		fmt.Println(<-ch)
	}
}
