#Socket programlamaya giriş, port tarama aracı yazımı
import socket
port_list = []
banner_list = []
file = open("ip.txt", "r")
ip_ = file.read()
file.close()
for ip in ip_.splitlines():
    print(ip)
    for port in range(1, 25):
        try:
            socket = socket.socket()
            socket.connect((str(ip), int(port)))
            banner = socket.recv(1024)
            # banner üçlü el sıkışmadan sonra servisin döndüğü bilgidir.
            banner_list.append(str(banner))
            port_list.append(str(port))
            socket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("The system can be a Linux or Network device.")
                log = str(ip)+"\n"
                file = open("linux.txt", "a")
                file.write(log)
                file.close()
        except:
            pass
print(port_list)
print(banner_list)


