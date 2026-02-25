package main

import (
	"fmt"

	amqp "github.com/rabbitmq/amqp091-go"
)

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

	q, err := ch.QueueDeclare(
		"TestQueue",
		false,
		false,
		false,
		false,
		nil,
	)

	if err != nil {
		panic(err)
	}
	
	fmt.Println(q)
	
	err = ch.Publish(
		"",
		"TestQueue",
		false,
		false,
		amqp.Publishing{
			ContentType: "text/plain",
			Body: []byte("This is the next message published"),
			
		},
	)
	
	if err != nil {
		panic(err)
	}
	
	fmt.Println("Successfully Published Message to Queue")
	
	

}
