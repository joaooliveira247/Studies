package goroutines

import (
	"fmt"
	"time"
)

func writeChannel(text string, ch chan string) {
	defer close(ch)

	for i := 0; i < 5; i++ {
		ch <- text
		time.Sleep(time.Second)
	}
}

func Channels() {
	ch := make(chan string)
	go writeChannel("Hello World", ch)
	for msg := range ch {
		fmt.Println(msg)
	}
}
