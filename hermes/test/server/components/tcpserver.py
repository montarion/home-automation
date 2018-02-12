from socket import *

class tcpcon():
    def __init__(self):
        pass

    def accept(self, portnumber):
        host = ""
        port = portnumber
        address = (host, port)
        TCPSock = socket(AF_INET, SOCK_STREAM)
        print('binding to: ' + str(address))
        TCPSock.bind(address)
        TCPSock.listen(2)

        for i in range(5):
            c, addr = TCPSock.accept()
            data = str(c.recv(1024))
            print('connection accepted from: ' + repr(addr[0]) + ' on port: ' + repr(addr[1]))
            print(str(data[2:-1]))
