#raspberry run
import socketio
import cups

queue = '/printer-queue'
sio = socketio.Client()
conn = cups.Connection()
printers = conn.getPrinters()
# def send_sensor_reading():
    # sio.emit('test', {'data': 'This is test data'}, namespace= queue)
    # sio.emit('joinClientQueue', namespace= queue)


@sio.on('connect')
def connect(namespace=queue):
    # sio.start_background_task(send_sensor_reading)
    print('connection established')
    sio.emit('test', {'data': 'This is a test data'}, namespace= queue)
    print('my sid is', sio.sid)
    
    # sio.emit('joinClientQueue', namespace= '/printer-queue')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.11.204:5000', headers={'tenantId':'1'},namespaces = ['/printer-queue'] )


print("abc")
for printer in printers:
    sio.emit('test', printer, namespace= queue)


printer_name=printers.keys()[0]
fileName = "hello.txt"
conn.printFile(printer_name, fileName, " ", {})