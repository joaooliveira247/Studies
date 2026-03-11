package main

import (
	"context"
	"fmt"
)

func printKeyValue(ctx context.Context) {
	fmt.Println(ctx.Value("testKey"))
}

// context.Background & context.TODO() are empty context struct
func main() {
	ctx := context.WithValue(
		context.Background(), "testKey", "testValue",
	)

	printKeyValue(ctx)
}
