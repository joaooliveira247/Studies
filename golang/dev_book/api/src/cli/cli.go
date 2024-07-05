package cli

import (
	"api/src/config"
	"api/src/db"
	"api/src/router"
	"fmt"
	"log"
	"net/http"

	"github.com/urfave/cli/v2"
)

func GenApp() *cli.App {
	app := &cli.App{
		Name:  "API CLI",
		Usage: "CLI to admin API",
		Commands: []*cli.Command{
			{
				Name:  "run",
				Usage: "Start API",
				Action: func(ctx *cli.Context) error {
					fmt.Println("Running API")
					r := router.GenRouter()
					log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", config.Port), r))
					return nil
				},
			},
			{
				Name:  "create-table",
				Usage: "Create all tables in database",
				Action: func(ctx *cli.Context) error {
					db.CreateTables()
					return nil
				},
			},
		},
	}
	return app
}
