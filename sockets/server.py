
import socket
import threading

PORT = 5050
SERVER = "192.168.0.5"
SERVER2 = socket.gethostbyname(socket.gethostname())

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


def handle_client(conn, addr):
    pass




                            





