package main

import (
	"context"
	"fmt"
	"time"
)

func printUntilTimeout(ctx context.Context) {
	count := 0

	for {
		select {
		case <-ctx.Done():
			fmt.Println("Cancel signal received, exiting")
			return

		default:
			time.Sleep(1 * time.Second)
			fmt.Printf("Printing until cancel, number = %d", count)
			count++
		}
	}
}

// context.Background & context.TODO() are empty context struct
func main() {
	ctx, cancel := context.WithTimeout(
		context.Background(), time.Second * 5,
	)

	defer cancel()

	printUntilTimeout(ctx)
}
