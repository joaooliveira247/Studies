package goroutines

import (
	"fmt"
	"sync"
)

func writeWaitGroup(text string) {
	for i := 0; i < 5; i++ {
		fmt.Println(text)
	}
}

func WaitGroup() {
	var waitGroup sync.WaitGroup

	waitGroup.Add(2)

	go func()  {
		writeWaitGroup("Hello")
		waitGroup.Done()
	}()

	go func()  {
		writeWaitGroup("World")
		waitGroup.Done()
	}()

	waitGroup.Wait()
}
