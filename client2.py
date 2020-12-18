#raspberry run
import socketio

sio = socketio.Client()
def send_sensor_reading():
    while True:
        sio.emit('connection',{'temp':75})
        sio.sleep(5)


@sio.event
def connect(namespace= '/printer-queue'):
    sio.start_background_task(send_sensor_reading)
    print('connection established')
    print('my sid is', sio.sid)
    
    

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000', namespaces = ['/printer-queue'])
