
import socket

HEADER = 64
PORT = 5050
FORMAT= 'utf-8'
DISCONNET_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

# setup the socket for the client
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)  # connect to the server at the port 


def send_message(msg):
    
    message= msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)

    send_length += b' ' * (HEADER - len(send_lenght))
    client.send(send_length)
    client.send(message)

send_message("hello world")













