import json

import pika


class RabbitMQPublisher:
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

    def send_message(
        self, exchange: str, message: dict, routing_key: str = ""
    ):
        self.__channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2),
        )


def main():
    publisher = RabbitMQPublisher("user", "password")
    publisher.send_message(
        "data_exchange", message={"msg": "Hello OO publisher"}
    )


if __name__ == "__main__":
    main()
