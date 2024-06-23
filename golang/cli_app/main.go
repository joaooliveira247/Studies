package main

import (
	"cli/app"
	"log"
	"os"
)

func main() {
	application := app.Gen()
	if err := application.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}
