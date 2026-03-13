package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var once sync.Once

	load := func() {
		fmt.Println("Exec init code")
	}

	for range 20 {
		wg.Add(1)
		wg.Go(
			func() {
				defer wg.Done()

				once.Do(load)
			},
		)
	}

	wg.Wait()
}
