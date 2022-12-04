import socket

new_socket = socket.socket()

new_socket.bind(('127.0.0.1', 55000))

name = 'Server'

new_socket.listen(1)

conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()

conn.send(name.encode())

while True:
    message = conn.recv(1024)
    message = message.decode()
    x=message.count(' ')+1
    conn.send(str(x).encode())
    print(client, ':', message)