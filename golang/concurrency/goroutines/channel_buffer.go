package goroutines

import "fmt"

func ChannelBuffer() {
	ch := make(chan string, 2)
	ch <- "Hello World!"
	ch <- "Hello Go"

	msg := <- ch
	msg2 := <- ch

	fmt.Println(msg, msg2)
}