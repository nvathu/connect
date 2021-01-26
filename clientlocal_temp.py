import socketio

sio = socketio.Client()
queue ='/printer-queue'

@sio.event
def connect():
    print('connection established')
    

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'},namespace=queue)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000',namespaces=[queue])
sio.wait()