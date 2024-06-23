package app

import (
	"fmt"
	"log"
	"net"

	"github.com/urfave/cli"
)

func searchIps(c *cli.Context) {
	host := c.String("host")

	ips, err := net.LookupIP(host)

	if err != nil {
		log.Fatal(err)
	}

	for _, ip := range ips {
		fmt.Println(ip)
	}
}

func searchServers(c *cli.Context) {
	host := c.String("host")

	servers, err := net.LookupNS(host)

	if err != nil {
		log.Fatal(err)
	}

	for _, server := range servers {
		fmt.Println(server.Host)
	}
}

// Return a pointer of App cli
func Gen() *cli.App {
	app := cli.NewApp()
	app.Name = "CLI application"
	app.Usage = "Search ip address and hostname"

	flags := []cli.Flag{
		cli.StringFlag{
			Name:  "host",
			Value: "google.com",
		},
	}

	app.Commands = []cli.Command{
		{
			Name: "ip",
			Usage: "Search ip address",
			Flags: flags,
			Action: searchIps,
		},
		{
			Name: "server",
			Usage: "Search hostname",
			Flags: flags,
			Action: searchServers,
		},
	}
	return app
}
