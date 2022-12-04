import socket

new_socket = socket.socket()

new_socket.bind(('127.0.0.1', 55000))

name = 'Server'

new_socket.listen(1)

conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()

conn.send(name.encode())

slovnik={'1+1':'2', '2+2':'4', '3+3':'6'}
while True:
    message = conn.recv(1024)
    message = message.decode()
    sendmess=slovnik[message]
    conn.send(sendmess.encode())
    print(client, ':', message)