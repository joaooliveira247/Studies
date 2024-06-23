package goroutines

import "fmt"

func write(text string) {
	for {
		fmt.Println(text)
	}
}
func Goroutines() {
	// concurrency != paralelism(Thread)
	go write("Hello World!")
	write("Running concurrent code")
}
