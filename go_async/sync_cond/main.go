package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex
	cond := sync.NewCond(&mu)

	ready := false

	// Goroutine que espera
	go func() {
		mu.Lock()
		for !ready {
			fmt.Println("Esperando ficar pronto...")
			cond.Wait() // libera o lock e espera
		}
		fmt.Println("Agora está pronto!")
		mu.Unlock()
	}()

	// Simula algum trabalho
	time.Sleep(2 * time.Second)

	mu.Lock()
	ready = true
	fmt.Println("Mudando estado para pronto")
	cond.Signal() // acorda uma goroutine
	mu.Unlock()

	time.Sleep(1 * time.Second)
}
