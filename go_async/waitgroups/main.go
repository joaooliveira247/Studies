package main

import (
	"fmt"
	"sync"
	"time"
)

func slowExecutation(t time.Duration) {
	fmt.Println("Start Method Executation")

	time.Sleep(t)

	fmt.Println("Finish Method Executation")
}

func main() {

	var wg sync.WaitGroup

	for range 5 {
		wg.Add(1)

		wg.Go(
			func() {
				slowExecutation(2 * time.Second)
			},
		)

		defer wg.Done()

	}

	wg.Wait()
}
