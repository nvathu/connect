import socketio
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('https://falcon.fl.office.com'))
channel = connection.channel()
channel.queue_declare(queue='print-notification')


sio = socketio.Client()

def send_sensor_readings():
    while True:
        sio.emit('my_message', {'temp':75})
        sio.sleep(5)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_sensor_readings)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000', headers={'device_id':'client1'})
