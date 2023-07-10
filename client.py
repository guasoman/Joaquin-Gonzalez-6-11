import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))


    client_socket.close()

HOST = '127.0.0.1'  
PORT = 8080  

start_client(HOST, PORT)

