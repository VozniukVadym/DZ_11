import socket

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)

name = 'client'

socket_server.connect(('127.0.0.1', 55000))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

while True:
    message = input("Client : ")
    socket_server.send(message.encode())
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)