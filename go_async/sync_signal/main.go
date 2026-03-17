package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func main() {
	// rand.Seed(time.Now().UnixNano())

	const N = 10
	var values [N]string

	cond := sync.NewCond(&sync.Mutex{})

	for i := range N {
		d := time.Second * time.Duration(rand.Intn(10)) / 10

		go func(i int) {
			time.Sleep(d)
			cond.L.Lock()
			values[i] = string('a' + i)
			cond.L.Unlock()
			cond.Signal()
		}(i)
	}

	checkCondition := func() bool {
		fmt.Println(values)
		for i := range N {
			if values[i] == "" {
				return false
			}
		}
		return true
	}

	cond.L.Lock()
	defer cond.L.Unlock()

	for !checkCondition() {
		cond.Wait()
	}
}
