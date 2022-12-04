import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',55000))
sock.send(bytes('hello world', encoding='UTF8'))
data = sock.recv(1024)
print(data)
sock.close()