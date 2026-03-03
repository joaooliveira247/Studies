package main

import (
	"fmt"
	"log"

	amqp "github.com/rabbitmq/amqp091-go"
)

const maxRetries = 3

func main() {

	conn, err := amqp.Dial("amqp://user:password@localhost:5672/")
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	ch, err := conn.Channel()
	if err != nil {
		log.Fatal(err)
	}
	defer ch.Close()

	msgs, err := ch.Consume(
		"TestQueue",
		"",
		false,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		log.Fatal(err)
	}

	forever := make(chan bool)

	go func() {
		for d := range msgs {

			retryCount := int64(0)

			if deaths, ok := d.Headers["x-death"].([]interface{}); ok {
				retryCount = deaths[0].(amqp.Table)["count"].(int64)
			}

			fmt.Printf("Message: %s | Tries: %d\n", d.Body, retryCount+1)

			if string(d.Body) == "error" {

				if retryCount >= maxRetries {
					fmt.Println("Max retries → sending to DLQ")

					err := ch.Publish(
						"dlx.exchange",
						"dlq",
						false,
						false,
						amqp.Publishing{
							ContentType: "text/plain",
							Body:        d.Body,
						},
					)
					if err != nil {
						log.Println("Erro ao publicar na DLQ:", err)
					}

					d.Ack(false)
					continue
				}

				fmt.Println("Erro → enviando para Retry")
				d.Nack(false, false) // manda para RetryQueue
				continue
			}

			d.Ack(false)
		}
	}()

	fmt.Println("[*] Waiting for messages")
	<-forever
}
