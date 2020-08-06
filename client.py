import socket
host = "127.0.0.1"
port  = 2121
with socket.socket() as socket:
    socket.connect((host,port))
    socket.sendall(b"Hello Cyber! ")
    data =socket.recv(1024)
print(data)