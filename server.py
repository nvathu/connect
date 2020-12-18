import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

#room 
@sio.event    
def begin_chat(sid):
   sio.enter_room(sid, 'chat_users')
    
@sio.event
def my_message(sid, data):
    sio.emit('my reply', "data", room='chat_users', skip_sid=NotImplemented)
    
@sio.event
def exit_chat(sid):
    sio.leave_room(sid, 'chat_users')

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)