package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var counter uint64
	var wg sync.WaitGroup

	for range 50 {
		wg.Add(1)

		wg.Go(func() {
			defer wg.Done()
			for range 1000 {
				atomic.AddUint64(&counter, 1)
			}
		})
	}

	wg.Wait()
	fmt.Printf("counter: %v\n", counter)
}
