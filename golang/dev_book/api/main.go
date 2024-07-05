package main

import (
	"api/src/cli"
	"api/src/config"
	"log"
	"os"
)

func main() {
	config.LoadEnv()
	if err := cli.GenApp().Run(os.Args); err != nil {
		log.Fatal(err)
	}
}
