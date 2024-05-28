from celery import Celery, shared_task
import pika
import os

app = Celery('tasks', broker=os.getenv("RABBITMQ_QUEUE"))

@app.task(bind=True)
def send_message_to_queue(self, message):
    try:
        connection = pika.BlockingConnection(pika.URLParameters(os.getenv("RABBITMQ_QUEUE")))
        channel = connection.channel()
        
        channel.queue_declare(queue='celery', durable=True)
        
        channel.basic_publish(
            exchange='celery',
            routing_key='celery',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        connection.close()
    except Exception as exception:
        print(f"[ERROR] - RABBITMQ EXCEPTION - {str(exception)}")
        raise self.retry(exc=error, countdown=10, max_retries=3)
