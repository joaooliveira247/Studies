package main

import (
	"fmt"
	"time"
)

func baseForLoop() {
	i := 0
	for i < 10 {
		time.Sleep(time.Second)
		fmt.Println(i)
		i++
	}
}

func forWithIfInit() {
	for j := 0; j < 10; j++ {
		fmt.Println(j)
	}
}

func forWithRange() {
	names := [3]string{"John", "Jane", "Peter"}
	for i, v := range names {
		fmt.Println(i, v)
	}

	for idx, letter := range "word" {
		fmt.Println(idx, letter) // letter will return ascii table value of letter
	}
}

func forIterByMap() {
	user := map[string]string{
		"name":     "John",
		"lastname": "Doe",
	}

	for k, v := range user {
		fmt.Println(k, v)
	}
}

func infinitLoop() {
	for {
		fmt.Println("Some thing")
	}
}

func main() {
	forIterByMap()
}
