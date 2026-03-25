package main

import (
	"fmt"
	"net/http"

	"golang.org/x/sync/errgroup"
)

func main() {
	var g errgroup.Group

	urls := []string{
		"https://golang.org",
		"https://google.com",
		"https://x.com",
	}

	for _, url := range urls {
		g.Go(func() error {
			resp, err := http.Get(url)

			if err != nil {
				return err
			}

			defer resp.Body.Close()

			fmt.Printf("Status From (%s): %s \n", url, resp.Status)

			return nil
		})
	}

	err := g.Wait()

	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("All requests success")
}
