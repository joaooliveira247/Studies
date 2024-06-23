package goroutines

import "fmt"

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-2) + fibonacci(n-1)
}

func workers(tasks <-chan int, results chan<- int) {
	for num := range tasks {
		results <- fibonacci(num)
	}
}

func WorkerPools() {
	tasks := make(chan int, 45)
	results := make(chan int, 45)

	go workers(tasks, results)
	go workers(tasks, results)
	go workers(tasks, results)
	go workers(tasks, results)

	for i := 0; i < 45; i++ {
		tasks <- i
	}
	close(tasks)

	for i := 0; i < 45; i++ {
		result := <- results
		fmt.Println(result)
	}
}
