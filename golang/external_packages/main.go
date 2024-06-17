package main

import (
	"fmt"
	"github.com/badoux/checkmail"
)

func main() {
	err := checkmail.ValidateFormat("dev@gmail.com")
	fmt.Println(err)
}