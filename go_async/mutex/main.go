package main

import (
	"fmt"
	"sync"
)

func main() {
	var counter uint64
	var wg sync.WaitGroup
	var mu sync.Mutex

	for range 50 {
		wg.Add(1)
		wg.Go(func() {
			defer wg.Done()
			for range 1000 {
				mu.Lock()
				counter++
				mu.Unlock()
			}
		})
	}

	wg.Wait()
	fmt.Printf("counter: %v\n", counter)
}
