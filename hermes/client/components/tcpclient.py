from socket import *


class sending:
    def __init__(self):
        pass

    def sendmsg(self, ip, msg):
        host = ip          # set to IP address of target computer
        port = 13333
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_STREAM)
        UDPSock.connect(addr)
        print('securely connected to ' + host)
        UDPSock.send(bytes(msg, "utf-8"))
        print('receiving')
        data = UDPSock.recv(1024)
        data = str(data)
        print(data[2:-1])
