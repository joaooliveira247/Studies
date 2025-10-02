import pika


def main():
    connection_params = pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials(
            username="user", password="password"
        ),
    )

    channel = pika.BlockingConnection(connection_params).channel()
    channel.basic_publish(
        "data_exchange",
        routing_key="",
        body="I'm sending a message",
        properties=pika.BasicProperties(
            delivery_mode=2
        ),
    )


if __name__ == "__main__":
    main()
