import pika


def my_callback(ch, method, properties, body):
    print(body)


def main():
    connection_params = pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials(
            username="user", password="password"
        ),
    )

    channel = pika.BlockingConnection(connection_params).channel()
    channel.queue_declare(queue="data_queue", durable=True)
    channel.basic_consume(
        queue="data_queue", auto_ack=True, on_message_callback=my_callback
    )

    print("Listen RabbitMQ on Port 5672")
    channel.start_consuming()


if __name__ == "__main__":
    main()
