from typing import Callable

import pika
import pika.channel


class RabbitMQConsumer:
    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 5672,
    ) -> None:
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_params = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username, password=self.__password
            ),
        )

        channel = pika.BlockingConnection(connection_params).channel()
        return channel

    def start_listener(self, queue: str, callback: Callable):
        self.__channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )
        print("Listen RabbitMQ on Port 5672")
        self.__channel.start_consuming()


def my_callback(ch, method, properties, body):
    print(body)


def main():
    consumer = RabbitMQConsumer("user", "password")
    consumer.start_listener("data_queue", my_callback)


if __name__ == "__main__":
    main()
