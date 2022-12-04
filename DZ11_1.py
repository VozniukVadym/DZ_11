import socket
import time

start_time=time.time()
print(str(start_time))
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',55000))
sock.listen(10)
print('server is running')
while True:
    conn, addr=sock.accept()
    print('connected: ', addr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data.upper())
conn.close()