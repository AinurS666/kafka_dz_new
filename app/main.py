from kafka import KafkaProducer, KafkaConsumer
import time

def produce_message():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    message = b"Hello, Kafka!"
    producer.send('test-topic', message)
    producer.flush()
    print('Сообщение отправлено: ', message.decode('utf-8'))  # Исправлено

def consume_message():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    for msg in consumer:
        print('Сообщение получено: ', msg.value.decode('utf-8'))  # Исправлено
        time.sleep(1)

if __name__ == '__main__':
    produce_message()
    time.sleep(2)

    consume_message()