import socketio

MAX_USERS = 1

num_of_users = 0
token_compiled = 'false'
users_tokens = np.array([])
users_headers = np.array([])

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')


@sio.on('data')
def response(*args):
    print(args)
    global users_tokens
    users_tokens = np.append(users_tokens, args)

    
#Token collections
def do_something_with_tokens(users_tokens):
    for i in range(MAX_USERS):
        global users_headers,num_of_users
#        sio.sleep(4)
        users_headers = np.append(users_headers, {"Authorization": "Bearer %s"%users_tokens[i]})    
        num_of_users = num_of_users+1

if __name__=="__main__":
    sio.connect('http://192.168.11.204:5000')
    sio.wait()