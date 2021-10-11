
import socket
import threading

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
#SERVER = "192.168.0.5"
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNET_MESSAGE = "!DISCONNECTING"

#print(SERVER)
#print('\n')
#print(SERVER2)
#print('\n')
#print(socket.gethostname())

ADDR = (SERVER,PORT)


'''Now let us create the socket & bind it to the address
 Socket allows us to open up this device to other connections'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.socket() is how we make a new Socket       
                                        # socket.socket() takes first argument as the family/category of sockets
                                        # AF_ represents Addres Family tells the socket what type of address should it look for    
                                        # SOCK_STREAM tells it will be a STREAM of data through this socket


'''When we bind our socket to an address, that addrss as to be in a tuple of server & the port asssociated'''                   
server.bind(ADDR)  # bind the socket to the address.. so anything which connnects to that addrss.. will hit this socket 


def handle_client(conn, addr):  # conn & addr would be the parameters
    print(f' [NEW CONNECTION]: {addr} connected!!')
    connected= True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   # just like server.accept() .. conn.recv() are BLOCKING lines of code.. so we do not pass these lines till the event they represent occur
        if msg_length:
            msg_length= int(msg_length)
            message= conn.recv(msg_length).decode(FORMAT)
            if message == DISCONNET_MESSAGE:
                #break
                connected= False

            print(f' \n [{addr}] {msg}')

        conn.close()

        
def start():
    # make the server listen to any connections & then handle those connections by passing them to handle_client()

    server.listen()
    print(f' [LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()  # server.accept() returns a tuple representing a new connection & the address of the client
                                      # serer.accept() BLOCKS .. we'll wait till a new connection occurs  
                                      # once a new connection occurs, start a new thread to handle the connection
        
        thread = threading.Thread(target= handle_client, args=(conn, addr))  # so when a new connection occurs, pass that connection to handle_client & pass the arguments
        thread.start()

        print(f'\n [ACTIVE CONNECTIONS]: {threading.activeCount()-1}')  # -1 to discount the main thread running on start()


print(" [STARTING] server is starting...") 
start()


                            





