package main

import (
	"fmt"
	"sync"
	"time"
)

var sharedRsc = false

func main() {
	var wg sync.WaitGroup

	m := sync.Mutex{}

	c := sync.NewCond(&m)

	wg.Go(func() {
		c.L.Lock()
		for sharedRsc == false {
			fmt.Println("goroutine 1 wait")
			c.Wait()
		}
		fmt.Println("goroutine 1", sharedRsc)
		c.L.Unlock()
		wg.Done()
	})

	wg.Go(func() {
		c.L.Lock()
		for sharedRsc == false {
			fmt.Println("goroutine 2 wait")
			c.Wait()
		}
		fmt.Println("goroutine 2", sharedRsc)
		c.L.Unlock()
		wg.Done()
	})

	time.Sleep(2 * time.Second)

	c.L.Lock()
	fmt.Println("main goroutine ready")
	sharedRsc = true
	c.Broadcast()
	fmt.Println("main goroutine broadcast")
	c.L.Unlock()

	wg.Wait()
}
