import socket
host = "127.0.0.1"
port = 2121
with socket.socket() as socket:
    socket.bind((host, port))
    socket.listen()
    conn, addr = socket.accept() #connection, address
    with conn:
        print("The connection has been made.", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


