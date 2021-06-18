import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='e6aa5455a6674d2', exchange_type='fanout'
)

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='e6aa5455a6674d2', queue=queue_name)

print('listening for messages...')

while True:
    for method_frame, _, body in channel.consume(queue_name):
        try:
            print(body)
        except OSError as error:
            print(error)
        else:
            channel.basic_ack(method_frame.delivery_tag)
