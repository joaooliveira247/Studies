package main

import (
	"fmt"

	amqp "github.com/rabbitmq/amqp091-go"
)

// Consumer
func main() {
	fmt.Println("Go RabbitMQ Teste")

	conn, err := amqp.Dial("amqp://user:password@localhost:5672/")

	if err != nil {
		panic(err)
	}

	defer conn.Close()

	fmt.Println("Successfully Connected To RabbitMQ instance.")

	ch, err := conn.Channel()

	if err != nil {
		panic(err)
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
	
	forever := make(chan bool)
	
	go func() {
		for d := range msgs {
			fmt.Printf("Recieved Message: %s\n", d.Body)
			
			if string(d.Body) == "error" {
				fmt.Println("Found Error -> Send to DLQ")
				d.Nack(false, false)
				continue
			}
		}
	}()
	
	fmt.Println("Successfully connectec to our RabbitMQ instance")
	fmt.Println("[*] - waiting for messages")
	<-forever
}
