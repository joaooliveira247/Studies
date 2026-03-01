package main

import (
	"fmt"
	"log"

	amqp "github.com/rabbitmq/amqp091-go"
)

func main() {
	fmt.Println("Go RabbitMQ Teste Producer")

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

	// =========================
	// Exchanges
	// =========================

	err = ch.ExchangeDeclare("main.exchange", "direct", true, false, false, false, nil)
	if err != nil {
		log.Fatal(err)
	}

	err = ch.ExchangeDeclare("retry.exchange", "direct", true, false, false, false, nil)
	if err != nil {
		log.Fatal(err)
	}

	err = ch.ExchangeDeclare("dlx.exchange", "direct", true, false, false, false, nil)
	if err != nil {
		log.Fatal(err)
	}

	// =========================
	// DLQ
	// =========================

	_, err = ch.QueueDeclare("DLQ", true, false, false, false, nil)
	if err != nil {
		log.Fatal(err)
	}

	err = ch.QueueBind("DLQ", "dlq", "dlx.exchange", false, nil)
	if err != nil {
		log.Fatal(err)
	}

	// =========================
	// Retry Queue (5 segundos)
	// =========================

	retryArgs := amqp.Table{
		"x-message-ttl":             int32(5000),
		"x-dead-letter-exchange":    "main.exchange",
		"x-dead-letter-routing-key": "main",
	}

	_, err = ch.QueueDeclare("RetryQueue", true, false, false, false, retryArgs)
	if err != nil {
		log.Fatal(err)
	}

	err = ch.QueueBind("RetryQueue", "retry", "retry.exchange", false, nil)
	if err != nil {
		log.Fatal(err)
	}

	// =========================
	// Main Queue
	// =========================

	mainArgs := amqp.Table{
		"x-dead-letter-exchange":    "retry.exchange",
		"x-dead-letter-routing-key": "retry",
	}

	_, err = ch.QueueDeclare("TestQueue", true, false, false, false, mainArgs)
	if err != nil {
		log.Fatal(err)
	}

	err = ch.QueueBind("TestQueue", "main", "main.exchange", false, nil)
	if err != nil {
		log.Fatal(err)
	}

	// =========================
	// Publicar mensagem
	// =========================

	err = ch.Publish(
		"main.exchange",
		"main",
		false,
		false,
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        []byte("error"),
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Infra criada e mensagem publicada com sucesso!")
}
