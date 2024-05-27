from celery import shared_task
import pika
import os

from celery import Celery

app = Celery('tasks', broker=os.getenv("RABBITMQ_QUEUE"))
@shared_task
def send_message_to_queue(message):
    cconnection = pika.BlockingConnection(pika.URLParameters(app.conf.broker_url))
    channel = connection.channel()
    channel.queue_declare(queue=os.getenv("QUEUE_NAME"))
    channel.basic_publish(
        exchange=os.getenv("EXCHANGE_NAME"),
        routing_key=os.getenv("QUEUE_NAME"),
        body=message
    )
    print(message)
    connection.close()
