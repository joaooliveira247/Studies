package main

import (
	"fmt"
	"log"

	amqp "github.com/rabbitmq/amqp091-go"
)

// Producer
func main() {
	fmt.Println("Go RabbitMQ Teste Producer")

	conn, err := amqp.Dial("amqp://user:password@localhost:5672/")

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	fmt.Println("Successfully Connected To RabbitMQ instance.")

	ch, err := conn.Channel()

	if err != nil {
		log.Fatal(err)
	}

	defer ch.Close()

	// Create DLX

	err = ch.ExchangeDeclare("dlx-exchange", "direct", true, false, false, false, nil)

	if err != nil {
		log.Fatal(err)
	}

	_, err = ch.QueueDeclare(
		"DeadLetterQueue",
		true,
		false,
		false,
		false,
		nil,
	)

	if err != nil {
		log.Fatal(err)
	}

	err = ch.QueueBind("DeadLetterQueue", "dlq-routing", "dlx-exchange", false, nil)

	if err != nil {
		log.Fatal(err)
	}

	args := amqp.Table{
		"x-dead-letter-exchange":    "dlx-exchange",
		"x-dead-letter-routing-key": "dlq-routing",
	}

	q, err := ch.QueueDeclare(
		"TestQueue",
		false,
		false,
		false,
		false,
		args,
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
			Body:        []byte("ok"),
		},
	)

	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully Published Message to Queue")

}
